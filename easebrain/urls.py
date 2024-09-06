from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from .views import UserView, signup, update_profile

app_name = 'easebrain'

urlpatterns = [
        # path('index', views.index, name='index'),
        path('login/', auth_views.LoginView.as_view(template_name='easebrain/login.html'), name='login'),
        path('logout/', auth_views.LogoutView.as_view(next_page='/easebrain/login'), name='logout'),
        path('profile/',  login_required(UserView.as_view()), name='profile'),
        path('signup/', signup, name='signup'),
        path('profile/update/', update_profile, name='update_profile'),
]
