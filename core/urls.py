from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('', include('video.urls')),
    path('rolex/', include('rolex.urls')),
    path('admin/', admin.site.urls),
]
