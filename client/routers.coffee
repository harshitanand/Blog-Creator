routes = (app) ->
  app.get '/*', (req, res)->
    res.render "#{__dirname}/assets/js/index"

module.exports = routes
