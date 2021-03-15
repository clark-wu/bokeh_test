const path = require('path');

module.exports = {
  entry: [
    './front/index.ts',
  ],
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: 'ts-loader',
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
        exclude: /node_modules/,

      },
    ],
  },
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dist'),
  },
  //mode: 'production',
  resolve: {
    extensions: ['.js', '.ts','.tsx']
  },
  mode: "development",
};