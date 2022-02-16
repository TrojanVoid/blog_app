from django.urls import path, include
from .views import index, user_login, user_logout, user_register, user_profile, change_password

urlpatterns = [
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('profile/', user_profile, name='user_profile'),
    path('password-change/', change_password.as_view(), name='password_change'),
    path('logout/', user_logout, name="logout")
]