from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from .views import UserView, signup, update_profile

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


app_name = 'easebrain'

urlpatterns = [
        # path('index', views.index, name='index'),
        path('login/', auth_views.LoginView.as_view(template_name='easebrain/login.html'), name='login'),
        path('logout/', auth_views.LogoutView.as_view(next_page='/easebrain/login'), name='logout'),

        # Token Authentication URLs
        path('jwt-login/', TokenObtainPairView.as_view(), name='jwt-login'),
        path('jwt-token-refresh/', TokenRefreshView.as_view(), name='jwt-token-refresh'),
        path('jwt-token-verify/', TokenVerifyView.as_view(), name='jwt-token-verify'),

        path('profile/',  login_required(UserView.as_view()), name='profile'),
        path('signup/', signup, name='signup'),
        path('profile/update/', update_profile, name='update_profile'),
]
