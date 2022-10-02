from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('mypolls/', include('mypolls.urls')),
    path('admin/', admin.site.urls),
]