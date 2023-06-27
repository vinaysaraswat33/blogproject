from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views
from .views import home, post,category
from .views import RegisterAPI
from django.urls import path

urlpatterns = [
    path('home/', home),
    path('blog/<slug:url>', post),
    path('category/<slug:url>',category),
path('api/register/', RegisterAPI.as_view(), name='register'),

]