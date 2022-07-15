const http = require('http')
const express = require('express')
const socketio = require('socket.io')
const swaggerJsDoc = require('swagger-jsdoc')
const swaggerUI = require('swagger-ui-express')

const swaggerDefinition = require('./docs/swaggerDefinitions')
const swaggerOptions = {
    swaggerDefinition,
    apis: ['./src/routes/**.js']
}
const swaggerDocs = swaggerJsDoc(swaggerOptions);

const userRouter = require('./routes/users')

const app = express()
app.use(express.json())
app.use(userRouter)
app.use('/api', swaggerUI.serve, swaggerUI.setup(swaggerDocs))

const server = http.createServer(app)
const io = socketio(server)

const port = process.env.PORT || 4000

io.of('/main').on('connection', (socket) => {
    // On connecting invoke the driver function to start the reading process
    console.log('SOCKET')
    socket.emit('catchMistake', 10)
})

app.get("*", (req, res) => {
    res.sendStatus(404);
})

server.listen(port, () => {
    console.log(`Server listening on port ${port}`)
})