// explanation: ...
const DotEnv = require('dotenv')

const parseEnv = DotEnv.config(
  {path:`.env.${process.env.NODE_ENV}`}
).parsed

module.exports = function (){
  return parseEnv
}

