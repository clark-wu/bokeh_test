const path = require('path');
const webpack = require('webpack')

module.exports = {
  entry: {
    index: './front/index.tsx',
    vendors: ["@bokeh/bokehjs"]
  },
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: 'ts-loader',
        exclude: /node_modules\/(?!@bokeh\/)/,
      },
      {
        test: /\.js?$/,
        include: path.join(__dirname, './front/'),
        use: [{
          loader: 'babel-loader',
          options: {
            presets: ["es2015", "stage-0", "react"]
          }
        }],
        exclude: /node_modules\/(?!@bokeh\/)/,

      },
    ],
  },
  output: {
    filename: '[name].js',
    path: path.resolve(__dirname, 'backend/dist'),
  },
  //mode: 'production',
  resolve: {
    extensions: ['.js', '.ts','.tsx']
  },
  mode: "development",
  devtool: 'eval-source-map',
  plugins: [
    new webpack.optimize.SplitChunksPlugin({
      name: "bokeh",
    })],
};
