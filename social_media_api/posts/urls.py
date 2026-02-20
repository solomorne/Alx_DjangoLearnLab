from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet,FeedView
from django.urls import path, include

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'feed', FeedView, basename='feed')

urlpatterns = router.urls + [
    path('feed/', FeedView.as_view(), name='feed'),
]
