from django.urls import path
from homepage.views import register, login_user, logout_user, homepage

app_name = "homepage"

urlpatterns = [
    path("", homepage, name="homepage"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
]
