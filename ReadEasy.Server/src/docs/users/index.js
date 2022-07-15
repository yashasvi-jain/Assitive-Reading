const getUsers = require('./get-users')

module.exports = {
    '/users': {
        ...getUsers
    }
}