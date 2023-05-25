from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from crud_app.views import PostViewSet

router = SimpleRouter()
router.register('posts', PostViewSet, basename='posts')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    
]
