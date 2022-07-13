const express = require('express');
const app = express();
const swaggerJsDoc = require('swagger-jsdoc');
const swaggerUI = require('swagger-ui-express');

const port = process.env.PORT || 4000;

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
        servers: ["http://localhost:4000"]
    },
    apis: ["app.js"]
};

const swaggerDocs = swaggerJsDoc(swaggerOptions);
app.use('/api-docs', swaggerUI.serve, swaggerUI.setup(swaggerDocs))

/**
 * @swagger
 * /data:
 *  get:
 *      tags: [Data]
 *      description: Use to request data
 *      responses:
 *          '200':
 *              description: Successful
 */
app.get("/data", (req, res) => {
    res.status(200).send("DATA");
});

/**
 * @swagger
 * /send:
 *  post:
 *      tags: [Data]
 *      description: Use to request data
 *      responses:
 *          '200':
 *              description: Successful
 */
app.post("/send", (req, res) => {
    console.log(req.query.data);
    res.status(200).send();
})

app.get("*", (req, res) => {
    res.sendStatus(404);
})

app.listen(port, () => {
    console.log(`Server listening on port ${port}`)
});