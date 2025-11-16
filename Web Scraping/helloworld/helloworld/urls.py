from django.contrib import admin
from django.urls import path
from hello.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworld/', index),  # Root URL shows Hello World
]
