angular.module 'blogapp'
  .controller 'PostCtrl',($scope, $http, $routeParams) ->
    $scope.post = null

    frmserv = null

    $scope.cancomment = true

    uri = 'http://localhost:8000/posts/' + $routeParams.id + '/'

    $http.get uri
      .success (data) ->
        $scope.post = data
        frmserv = data

    $scope.formshow = ->
      $scope.cancomment = not $scope.cancomment

    $scope.liked = ->
      frmserv.likes++
      $http.patch uri,frmserv
        .success (data) ->
          $scope.post = data

    $scope.addcomment = ->
      if $scope.comment is undefined or $scope.author is undefined
        return
      comment = 
        body: $scope.comment
        author: $scope.author

      frmserv.comments.push(comment)
      $http.put uri,frmserv
        .success (data) ->
          $scope.post = data
      $scope.cancomment = not $scope.cancomment

