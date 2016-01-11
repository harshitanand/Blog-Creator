require('coffee-script/register');
var express = require('express');

bodyParser = require("body-parser");
cookieParser = require('cookie-parser');
methodOverride = require('method-override');

errorHandler = require('errorhandler');
helmet = require('helmet');

var csrf = require ('csurf');

var app;

app = module.exports = express();
app.set('trust proxy',1);
app.disable('x-powered-by');

app.use(cookieParser());
app.set('view engine', 'jade');


app.use(express.static(__dirname + '/assets'));

webappRouter = express.Router();
webappRoutes = require('./routers')(webappRouter);
app.use('/',webappRoutes);

var server = null;
server = require('http').createServer(app);
//port = require('./port');
packageJ= require('./package.json');
server.listen(3000,function(){
  console.log("%s version %s running on port %d in %s mode",packageJ.name, packageJ.version, 3000, app.settings.env);
  console.log('Server\'s UID is now ' + process.getuid());
});
