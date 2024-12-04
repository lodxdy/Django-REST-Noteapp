from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),       # Admin site
    path('', include('notes.urls')),      # Include notes app routes
]
