from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from rest_framework_mongoengine.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from Blog.serializers import UserSerializer, PostSerializer
from Blog.models import Post 

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class PostList(ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class PostDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
