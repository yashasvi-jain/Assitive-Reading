const express = require('express')
const User = require('../models/users')
const auth = require('../middleware/auth')
const router = new express.Router()
const { spwan } = require('child_process')

// User login endpoint
router.post('/users/login', async (req, res) => {
    try {
        const user = await User.findByCredentials(req.body.email, req.body.password)
        const token = await user.generateAuthToken()
        res.send({ user, token })
    } catch (e) {
        res.sendStatus(400)
    }
})

// User logout endpoint
router.post('/users/logout', auth, async (req, res) => {
    try {
        req.user.tokens = req.user.tokens.filter((token) => {
            return token.token !== req.token
        })
        await req.user.save()
        res.send()
    } catch (e) {
        res.sendStatus(500)
    }
})

// User logout all sessions endpoint
router.post('/users/logoutAll', auth, async (req, res) => {
    try {
        req.user.tokens = []
        await req.user.save()
        res.send()
    } catch (e) {
        res.sendStatus(500)
    }
})

// Retrieve list of all users
router.get('/users', async (req, res) => {
    try {
        // spwan('python3', ['../../ReadEasy.MainDriver/main.py'])
        return res.status(200).send("Hello")
    } catch (e) {
        res.sendStatus(500)
    }
})

// Retrieve single user based on id
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

router.get('/users/me', auth, async (req, res) => {
    res.send(req.user)
})

// Create user
router.post('/users', async (req, res) => {
    const user = new User(req.body)

    try {
        await user.save()
        const token = await user.generateAuthToken()
        res.status(201).send({ user, token })
    } catch (e) {
        res.sendStatus(400)
    }
})

// Delete user
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