const express = require('express')
const router = express.Router()
const swaggerOptions = require('../docs/swaggerOptions')
const swaggerDocs = swaggerJsDoc(swaggerOptions);

router.use('/api-docs', swaggerUI.serve, swaggerUI.setup(swaggerDocs))

module.exports = router