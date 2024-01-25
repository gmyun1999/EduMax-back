"""config URL Configuration

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
from django.contrib import admin
from django.urls import path, re_path, include


from community.views import PostView, LikeView, GetPostsView

urlpatterns = [

    path("admin/", admin.site.urls),
    path("auth/", include("account.urls")),
  # path('posts/<int:post_id>/likes', LikeView.as_view()),
    path('post/<int:post_id>', PostView.as_view()),
    path('post/', PostView.as_view()),
    path('posts/', GetPostsView.as_view())
]

handler404 = "config.exceptions.custom_exception_views.url_not_found"