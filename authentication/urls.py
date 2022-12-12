from django.urls import path
from authentication.views import register_user, login_user, logout_user

app_name = "authentication"

urlpatterns = [
    path("register/", register_user, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
]
