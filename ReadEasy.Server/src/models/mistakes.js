const mongoose = require('mongoose')

const Mistakes = mongoose.model('Mistakes', {
    replacements: {
        type: mixed,
    },
    insertions: {
        type: Array
    },
    omissions: {
        type: mixed
    },
    misplacements: {
        type: Array
    }
})

module.exports = Mistakes