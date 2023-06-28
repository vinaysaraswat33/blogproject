from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views
from .views import home, post,category, login, signup
from .views import RegisterAPI

app_name='blog'
urlpatterns = [
    path('home/', home),
    path('blog/<slug:url>', post),
    path('category/<slug:url>',category),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('api/register/', RegisterAPI.as_view(), name='register'),

]