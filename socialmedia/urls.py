"""
URL configuration for socialmedia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from social.views import delete_post
from social.views import (
    home,
    register,
    user_login,
    user_logout,
    profile,
    create_post,
    like_post,
    add_comment,
    follow_user,
    delete_post
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),

    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),

    path('profile/', profile, name='profile'),
    path('create-post/', create_post, name='create_post'),
path('like/<int:post_id>/', like_post, name='like_post'),
path('comment/<int:post_id>/', add_comment, name='add_comment'),
path('follow/<int:user_id>/', follow_user, name='follow_user'),
path('delete-post/<int:post_id>/', delete_post, name='delete_post'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)