const express = require('express')
const router = new express.Router()

/**
 * @swagger
 * /users:
 *  get:
 *      summary: Retrieve a list of all users
 *      description: Retrieve a list of all users
 *      tags: [User Data]
 *      responses:
 *          200:
 *              description: Success
 */
router.get('/users', async (req, res) => {
    try {
        res.status(200).send("Hello")
    } catch (e) {
        res.sendStatus(500)
    }
});

module.exports = router