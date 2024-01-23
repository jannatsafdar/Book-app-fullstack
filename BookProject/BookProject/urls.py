from django.contrib import admin
from django.urls import path, include
from bookapp.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('bookapp.urls')),  # Add your app name here
    
]
