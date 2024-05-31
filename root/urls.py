from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authtoken import views

from root import settings

schema_view = get_schema_view(
    openapi.Info(
        title="P19 API",
        default_version='v1',
        description="something",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True, permission_classes=(permissions.AllowAny,),
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
                  path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  path("admin/", admin.site.urls),
                  path("api/v1/", include('apps.urls')),
                  path('api-auth/', include('rest_framework.urls')),

                  path('api-token-auth/', views.obtain_auth_token),  # token based

                  # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)
