from django.urls import path

from .api_views import AdListAPIView, AdCreateAPIView, AdDetailAPIView, AdUpdateAPIView, AdDeleteAPIView, \
    CommentListAPIView, CommentDetailAPIView, CommentCreateAPIView, CommentUpdateAPIView, CommentDeleteAPIView
from .apps import SalesConfig

app_name = SalesConfig.name

urlpatterns = [
    # ads routes
    path('ads/', AdListAPIView.as_view(), name='ads-list'),
    path('ads/me/', AdListAPIView.as_view(), name='ads-me'),
    path('ads/<int:id>/', AdDetailAPIView.as_view(), name='ads-detail'),
    path('ads/create/', AdCreateAPIView.as_view(), name='ads-create'),
    path('ads/update/<int:id>/', AdUpdateAPIView.as_view(), name='ads-update'),
    path('ads/delete/<int:id>/', AdDeleteAPIView.as_view(), name='ads-delete'),

    # comments routes
    path('ads/<int:id>/comments/', CommentListAPIView.as_view(), name='comments-list'),
    path('ads/<int:id>/comments/<int:commentId>/', CommentDetailAPIView.as_view(), name='comments-detail'),
    path('ads/<int:id>/comments/create/', CommentCreateAPIView.as_view(), name='comments-create'),
    path('ads/<int:id>/comments/update/<int:commentId>/', CommentUpdateAPIView.as_view(), name='comments-update'),
    path('ads/<int:id>/comments/delete/<int:commentId>/', CommentDeleteAPIView.as_view(), name='comments-delete'),
]
