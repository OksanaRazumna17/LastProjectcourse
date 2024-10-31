from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.http import HttpResponse
from myapp.views import ProtectedView  # Імпортуємо наше представлення
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from myapp.views import UserViewSet

# Просте представлення для домашньої сторінки
def home(request):
    return HttpResponse("Welcome to the homepage!")

# Налаштування Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="Документація для нашого API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Налаштування маршрутизатора для UserViewSet
router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/protected/', ProtectedView.as_view(), name='protected_view'),  # Захищений ендпоінт
    path('', home, name='home'),  # Домашня сторінка
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # Redoc
    path('', include(router.urls)),  # Додаємо маршрути для UserViewSet
]
