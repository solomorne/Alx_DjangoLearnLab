from rest_framework.routers import DefaultRouter
from .views import LikePostView, PostViewSet, CommentViewSet,FeedView
from django.urls import path, include

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = router.urls + [
    path('feed/', FeedView.as_view(), name='feed'),
    path('posts/<int:pk>/', LikePostView.as_view(), name='like-post'),
]
