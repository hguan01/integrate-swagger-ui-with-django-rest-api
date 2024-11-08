from django.urls import path
from .views import BookAPI, BookDetailedAPI
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Books API",
      default_version='1.0',
      description="Swagger UI with Django REST API",
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   url="http://127.0.0.1:8000/api",
)

urlpatterns = [
    path('books/', BookAPI.as_view(), name="Books"),
    path('books/<int:id>/', BookDetailedAPI.as_view(), name='UpdateBooks'),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='SchemaJSON'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='SchemaSwaggerUI'),
]