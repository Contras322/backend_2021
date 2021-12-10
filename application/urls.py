"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from movies.views import MovieViewSet
from comments.views import CommentViewSet
from genres.views import GenreViewSet
from django.contrib.auth import views as auth_views
from application.views import auth

router = DefaultRouter()
router.register(r'api/movies', MovieViewSet, basename='movies')
router.register(r'api/comments', CommentViewSet, basename='comments')
router.register(r'api/genres', GenreViewSet, basename='genres')


urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    url('', include('social_django.urls', namespace='social')),
    path('auth/', auth),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
]

urlpatterns += router.urls
