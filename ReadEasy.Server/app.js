const http = require('http')
const express = require('express')
const socketio = require('socket.io')

const app = express()
app.use(express.json())
const server = http.createServer(app)
const io = socketio(server)

const port = process.env.PORT || 4000

/**
 * @swagger
 * /send:
 *  post:
 *      tags: [Data]
 *      description: Use to request data
 *      responses:
 *          '200':
 *              description: Successful
 */
app.post("/send", (req, res) => {
    console.log(req.query.data);
    res.status(200).send();
})

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