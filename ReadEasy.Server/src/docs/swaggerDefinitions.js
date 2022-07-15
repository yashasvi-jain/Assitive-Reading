// Extended: https://swagger.io/specification/#infoObject
const swaggerDefinition = {
    openapi: "3.0.0",
    info: {
        title: "ReadEasy.API",
        description: "User data",
        version: "1.0.0",
        contact: {
            name: "Yashasvi Jain",
            email: "me.yashassvijain@gmail.com"
        }
    },
    responses: {
        '200': {
            description: 'Success'
        }
    },
    servers: [
        {
            url: 'http://localhost:4000',
            description: 'Development server',
        },
    ]
};

module.exports = swaggerDefinition