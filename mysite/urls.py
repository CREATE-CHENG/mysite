"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from articles.views import ArticleViewSet, CategoryViewSet, ArchiveViewSet
from users.views import SocialToJwtView, CheckPermissionView
from comments.views import ImageUploadViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'articles', ArticleViewSet, base_name='articles')
router.register(r'categories', CategoryViewSet, base_name='categories')
router.register(r'archive', ArchiveViewSet, base_name='archive')
router.register(r'images', ImageUploadViewSet, base_name='image')
router.register(r'comments', CommentViewSet, base_name='comments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/check_permission/', CheckPermissionView.as_view()),
    path('api/social_to_jwt/', SocialToJwtView.as_view()),
    path('', include('social_django.urls', namespace='social')),
    path('', TemplateView.as_view(template_name='index.html'), name='index')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
