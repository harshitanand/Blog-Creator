// Generated by CoffeeScript 1.10.0
(function() {
  angular.module('blogapp').controller('MainCtrl', function($scope, $http, $location) {
    $scope.message = "This is choot";
    $scope.posts = null;
    $http.get('http://localhost:8000/posts/').success(function(data) {
      console.log(data);
      return $scope.posts = data.results;
    });
    return $scope.more = function(id) {
      return $location.path('/posts/' + id);
    };
  });

}).call(this);
