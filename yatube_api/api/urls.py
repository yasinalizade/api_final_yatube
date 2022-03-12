from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()

router.register(r'posts', PostViewSet, basename='text')
router.register(r'groups', GroupViewSet)
router.register(r'follow', FollowViewSet, basename='follow')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)

urlpatterns = [
    path('v1/', include(router.urls), name='api_v1'),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
