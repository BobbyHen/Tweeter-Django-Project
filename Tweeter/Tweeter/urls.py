"""Tweeter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profiles/<str:username>/', user_views.profile, name='profile'),
    path('dashboard/', user_views.Dashboard.as_view(), name='dashboard'),
    path('tweet/<int:pk>/', user_views.TweetDetail.as_view(), name='tweet-detail'),
    path('compose/', user_views.ComposeTweet.as_view(), name='compose'),
    path('allusers/', user_views.allusers, name='allusers'),
    path('settings/', user_views.settings, name='settings'),
    path('', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)