const express = require('express')
const router = new express.Router()
const User = require('../models/users')


router.get('/users', async (req, res) => {
    try {
        return res.status(200).send("Hello")
    } catch (e) {
        res.sendStatus(500)
    }
})

router.get('/users/:id', async (req, res) => {
    const _id = req.params.id

    try {
        const user = await User.findById(_id)

        if (!user){
            return res.sendStatus(404)
        }

        res.send(user)
    } catch (e) {
        res.sendStatus(500)
    }
})

router.post('/users', async (req, res) => {
    const user = new User(req.body)

    try {
        await user.save()
        res.status(201).send(user)
    } catch (e) {
        res.sendStatus(400)
    }
})

router.delete('/users/:id', async (req, res) => {
    const _id = req.params.id
    try {
        const user = await User.findByIdAndDelete(_id)

        if (!user) {
            return res.sendStatus(404)
        }

        res.send(user)
    } catch (e) {
        res.sendStatus(500)
    }
})

module.exports = router