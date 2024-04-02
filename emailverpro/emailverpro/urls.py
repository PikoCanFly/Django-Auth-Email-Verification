from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("accounts/register/", register_user, name="register"),
    path("activate/<str:uidb64>/<str:token>/", activate, name="activate"),
    path("accounts/", include("django.contrib.auth.urls"))
]
