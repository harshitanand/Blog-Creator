angular.module 'blogapp'
  .controller 'MainCtrl', ($scope, $http, $location) ->
    $scope.message = "This is choot"
    $scope.posts = null

    $http.get('http://localhost:8000/posts/').success (data) ->
      console.log data
      $scope.posts = data.results

    $scope.more = (id) ->
      $location.path '/posts/'+id
    
