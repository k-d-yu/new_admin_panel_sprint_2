from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('_debug_/', include('debug_toolbar.urls')),
    path('api/', include('movies.api.urls')),
]
