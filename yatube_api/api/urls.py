from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView
)

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet, basename='posts')
router_v1.register('groups', GroupViewSet, basename='groups')
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router_v1.register('follow', FollowViewSet, basename='follow')

jwt_patterns = [
    path('create/', TokenObtainPairView.as_view(), name='jwt-create'),
    path('refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    path('verify/', TokenVerifyView.as_view(), name='jwt-verify'),
]

urlpatterns = [
    path('v1/jwt/', include(jwt_patterns)),
    path('v1/', include(router_v1.urls)),
]
