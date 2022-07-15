module.exports = {
    get: {
        tags:["User Data"],
        description: "Retrieve a list of all users",
        summary: "Retrieve a list of all users",
        responses: {
            '200': {
                description: "Success",
                content: {
                    'application/json': {
                        schema: {
                            $ref: "#/components/schemas/User"
                        }
                    }
                }
            }
        }
    }
}