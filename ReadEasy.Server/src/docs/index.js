// Extended: https://swagger.io/specification/#infoObject
// Refer: https://www.section.io/engineering-education/documenting-node-js-rest-api-using-swagger/
// Refer: https://www.webfx.com/web-development/glossary/http-status-codes/

const swaggerDefinition = require('./swaggerDefinition')
const components = require('./components');
const servers = require('./servers')
const tags =  require('./tags')
const users = require('./users')

module.exports = {
    ...swaggerDefinition,
    ...components,
    ...servers,
    ...tags,
    paths: {
        ...users
    },
    //apis: ['./src/routes/**.js']
}