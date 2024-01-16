from django.urls import path, include
from djoser.views import UserViewSet

from .apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    # djoser routes
    path('users/', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='register'),
    path('users/me/',
         UserViewSet.as_view({'get': 'me', 'put': 'me', 'patch': 'me', 'delete': 'me'}),
         name='current_user_detail'),
    path('users/reset_password/', UserViewSet.as_view({'post': 'reset_password'}), name='reset_password'),
    path('users/reset_password_confirm/', UserViewSet.as_view({'post': 'reset_password_confirm'}),
         name='reset_password_confirm'),
    path('users/set_password/', UserViewSet.as_view({'post': 'set_password'}), name='change_password'),
    path('users/<int:id>/',
         UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='user_detail'),
    path('', include('djoser.urls.jwt')),  # for work with JWT
]
