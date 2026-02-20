from rest_framework.routers import DefaultRouter
from .views import LikePostView, PostViewSet, CommentViewSet,FeedView, UnlikePostView
from django.urls import path, include

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = router.urls + [
    path('feed/', FeedView.as_view(), name='feed'),
    path('posts/<int:pk>/', LikePostView.as_view(), name='like-post'),
    path('<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    path('<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
]
