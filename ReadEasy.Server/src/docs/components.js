const m2s = require('mongoose-to-swagger')
const User = require('../models/users')
const userSchema = m2s(User)

module.exports = {
    components: {
        schemas: {
            User: userSchema
        }
    }
}