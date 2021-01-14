'use strict';

import babel from 'rollup-plugin-babel';

export default {
  entry: './src/index.js',
  format: 'iife',
  plugins: [
    babel({
      exclude: './node_modules/**',
      presets: [
        [ "es2016" ]
      ],
      plugins: [
        "external-helpers"
      ],
      runtimeHelpers: true,
      babelrc: false
    })
  ],
  dest: './dist/gif-360.es6.js',
  sourceMap: true
};
