from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework_mongoengine.serializers import DocumentSerializer
from Blog.models import Post

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class PostSerializer(DocumentSerializer):
    class Meta:
        model = Post
        depth = 5

