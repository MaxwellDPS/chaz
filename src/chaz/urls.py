import durin.views

from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic.base import RedirectView

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from drf_yasg.generators import OpenAPISchemaGenerator

from rest_framework import permissions

class BothHttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ["http", "https"]
        return schema

SchemaView = get_schema_view(
   openapi.Info(
      title="CHAZ API",
      default_version='v1',
      description="CHAOTIC READY",
      license=openapi.License(name="AGPLv3 License"),
   ),
   public=True,
   generator_class=BothHttpAndHttpsSchemaGenerator,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
   path('', RedirectView.as_view(url='/api/v1', permanent=False)),
   re_path(r'^api/$', RedirectView.as_view(url='/api/v1', permanent=False)),
   re_path(r'^api/v1/$', SchemaView.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('api/v1/auth/login/', durin.views.LoginView.as_view(), name='durin_login'),
   path('api/v1/auth/refresh/', durin.views.RefreshView.as_view(), name='durin_refresh'),
   path('api/v1/auth/logout/', durin.views.LogoutView.as_view(), name='durin_logout'),
   path('api/v1/auth/logoutall/', durin.views.LogoutAllView.as_view(), name='durin_logoutall'),
   path('api/v1/', include('the_thing.urls')),
   path('admin/', admin.site.urls),
]
