// #region Imports

// Server Modules
const http = require('http')
const express = require('express')
const socketio = require('socket.io')

// Swagger Modules
const swaggerJsDoc = require('swagger-jsdoc')
const swaggerUI = require('swagger-ui-express')
const docs = require('./docs')

// DB init
//require('./db/mongoose')

// Routers
const userRouter = require('./routes/users')

// Other stuff
const {spawn} = require('child_process')

// #endregion

const app = express()
app.use(express.json())
app.use(userRouter)
app.use('/api', swaggerUI.serve, swaggerUI.setup(docs))

const server = http.createServer(app)
const io = socketio(server)

const port = process.env.PORT || 4000

io.of('/main').on('connection', (socket) => {
    // On connecting invoke the driver function to start the reading process
    console.log('Connected to Main Namespace')
    socket.emit('read', 'This is the paragraph.')
    socket.on('transfer', (data) => {
        console.log(data)
    })
})

app.get("*", (req, res) => {
    res.sendStatus(404);
})

server.listen(port, () => {
    console.log(`Server listening on port ${port}`)
})

// const main = async () => {
//     const python = spawn('python3', ['../ReadEasy.MainDriver/main.py'])
// }
// main()