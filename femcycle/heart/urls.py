from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UserDataViewSet, UserLoginView, UserRegistrationView, ProfileViewSet


router = DefaultRouter()
router.register(r'user-data', UserDataViewSet)
router.register(r'profiles', ProfileViewSet)


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
     path('login/', UserLoginView.as_view(), name='login'),
] + router.urls