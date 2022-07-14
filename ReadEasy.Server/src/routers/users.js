const express = require('express')
const router = express.Router()

/**
 * @swagger
 * /users:
 *  get:
 *      tags: [User]
 *      description: Use to list of all users
 *      responses:
 *          '200':
 *              description: Successful
 */
router.get('/users', async (req, res) => {
    try {
        res.status(200).send()
    } catch (e) {
        res.sendStatus(500)
    }
})

module.exports = router