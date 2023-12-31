from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView
from users.api.views import UserApiViewSet, UserApiView


router_user = DefaultRouter()

router_user.register(prefix='users', basename='users', viewset=UserApiViewSet)

urlpatterns = [
    path('auth/me/', UserApiView.as_view(), name='me'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair')
]