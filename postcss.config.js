const path = require('path');

const config = {
    plugins: {
        'postcss-import': {
            path: [
                path.join(__dirname, 'node_modules'),
                path.join(__dirname)
            ],
        },
        'postcss-cssnext': {}
    },
};

module.exports = config;