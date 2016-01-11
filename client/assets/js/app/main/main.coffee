angular.module 'blogapp'
  .config ($routeProvider) ->
    $routeProvider
      .when '/',
        templateUrl: '/js/app/main/main.html'
        controller: 'MainCtrl'
      .when '/posts/:id',
        templateUrl: '/js/app/posts/posts.html'
        controller: 'PostCtrl'
