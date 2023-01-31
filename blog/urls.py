"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

# MEDIA CONFIG (RESIM DESTEGI)
from django.conf import settings
from django.conf.urls.static import static

# post uygulamasındaki viewleri dahil et
from post.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="anasayfa"),
    path('posts/<slug:slug>/', post, name='singlePost'),
    path('post/create', createPost, name="handleCreatePost"),
    path('register', userRegister, name="user-register"),
    path('login', userLogin, name="user-login"),
    path('logout', userLogout, name="user-logout"),
    path('comments/delete/<id>', deleteComment, name="delete-comment"),
    path('comments/update/<id>', updateComment, name="update-comment")



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
