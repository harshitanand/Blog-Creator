angular.module 'blogapp',[
  'ngCookies',
  'ngResource',
  'ngSanitize',
  'ngRoute',
  'ui.bootstrap'
]
  .config ($routeProvider, $locationProvider, $httpProvider) ->
    $routeProvider
      .otherwise
        redirectTo: '/'

    $locationProvider.html5Mode true
