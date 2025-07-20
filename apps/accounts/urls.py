from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
     TokenRefreshView,
     TokenVerifyView,
     TokenBlacklistView
 )
from .views import UserViewset, TokenObtainPairView

router = DefaultRouter()
router.register(r"users", UserViewset, basename="users")


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
] + router.urls