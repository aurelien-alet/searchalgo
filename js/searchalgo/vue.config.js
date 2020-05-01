module.exports = {
    pluginOptions: {
        electronBuilder: {
            builderOptions: {
                compression: "maximum",
                productName: "SearchAlgo",
                files: [
                    "!**/node_modules/.cache"
                ],
                linux: {
                    target: "AppImage",
                    category: "Utility"
                }
            }
        }
    }
}