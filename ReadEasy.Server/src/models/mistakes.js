const mongoose = require('mongoose')

const MistakesDTOSchema = mongoose.Schema({
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
}, {
    timestamps: true
})

const Mistakes = mongoose.model('Mistakes', MistakesDTOSchema)

module.exports = Mistakes