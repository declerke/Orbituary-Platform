from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_obituary, name='submit_obituary'),
    path('', views.view_obituaries, name='view_obituaries'),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('obituaries.urls')),
]
