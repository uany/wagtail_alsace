const path = require('path');

const webpack = require('webpack');

const ExtractTextPlugin = require('extract-text-webpack-plugin');
const CleanWebpackPlugin = require('clean-webpack-plugin');
const LiveReloadPlugin = require('webpack-livereload-plugin');
const HtmlWebpackPlugin = require('html-webpack-plugin');

const isProd = process.env.NODE_ENV === 'production';
console.log('Building for: ', process.env.NODE_ENV);

const extractCss = new ExtractTextPlugin({
    filename:  (isProd)
            ? './css/[name].[hash].css'
            : './css/[name].css'
    }
);

const config = {
    context: path.resolve(__dirname),
    mode: process.env.NODE_ENV,
    entry: './src/index.js',
    devtool: 'cheap-module-source-map',
    output: {
        path: path.resolve(__dirname, 'static'),
        filename: (isProd) ? './js/alsace.[hash].js' : './js/alsace.js',
        publicPath: '/static/'
    },
    stats: {
        colors: true,
        chunks: true,
        children: false,
        optimizationBailout: true,
        maxModules: 5
    },
    module: {
        rules: [
            {
                test: /\.js?$/,
                use: ['babel-loader'],
                exclude: /node_modules/
            },
            {
                test: /\.css$/,
                use: extractCss.extract({
                    fallback: 'style-loader',
                    use: ['css-loader', 'postcss-loader']
                })

            },
            {
                test: /\.(png|jpg|gif|svg|eot|otf|ttf|woff|woff2)$/,
                loader: 'url-loader',
                options: {
                    limit: 24
                }
            }
        ]
    },
    plugins: [
        extractCss,
        new CleanWebpackPlugin([
            './static/js/*.*',
            './static/css/*.*'
        ]),
        new webpack.ProvidePlugin({
            $: 'jquery'
        }),
        new HtmlWebpackPlugin({
            filename: path.join(__dirname, './base/templates/base.html'),
            template: path.join(__dirname, './base/templates/base.template.html'),
            hash: false
        })
    ],
};

if(!isProd){
    config.plugins.push(
        new LiveReloadPlugin({
            appendScriptTag: true
        })
    )
}

module.exports = config;
