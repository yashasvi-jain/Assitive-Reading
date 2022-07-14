// Extended: https://swagger.io/specification/#infoObject
const swaggerOptions = {
    swaggerDefinition: {
        info: {
            title: "ReadEasy.API",
            description: "User data",
            contact: {
                name: "Yashasvi Jain"
            }
        },
        tags: {
            name: 'Data'
        },
        responses: {
            '200': {
                description: 'Success'
            }
        },
        //servers: ["http://localhost:4000"]
    },
    apis: ["../routers*.js"]
}

module.exports = swaggerOptions