from django.contrib import admin
from django.urls import path
from blog.views import *
from blog2.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index),
    path('posts/', post_list),
    path('posts/<int:post_id>/', post_detail),
    path('posts/add/', post_add),
]

urlpatterns += static(
    prefix = settings.MEDIA_URL,
    document_root = settings.MEDIA_ROOT,
)
