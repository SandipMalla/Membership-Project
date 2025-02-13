from django.urls import path, include
from .viewsets import CustomUserViewSet
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'', CustomUserViewSet)
   
urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]