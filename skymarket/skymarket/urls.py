from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    # admin panel django
    path("admin/", admin.site.urls),

    # apps routing
    path('api/', include('users.urls', namespace='user')),
    path('api/', include('ads.urls', namespace='ads')),

    # drf spectacular documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
]
