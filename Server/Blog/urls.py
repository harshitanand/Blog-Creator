from django.conf.urls import patterns, include, url
from rest_framework import routers
from Blog.views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns =[
    # Examples:
    # url(r'^$', 'Blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(router.urls)),
    url(r'^posts/$', PostList.as_view()),
    url(r'^posts/(?P<id>[\w]{24})/$', PostDetails.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
