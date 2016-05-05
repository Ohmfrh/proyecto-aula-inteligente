"""aula URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^home/', include('home.urls', namespace='home', app_name='home')),
    url(r'^usuarios/', include('usuarios.urls', namespace='usuarios', app_name='usuarios')),
    url(r'^identificacion/', include('identificacion.urls', namespace='identificacion', app_name='identificacion')),
    url(r'^musica/', include('musica.urls', namespace='musica', app_name='musica')),
    url(r'^imagenes/', include('imagenes.urls', namespace='imagenes', app_name='imagenes')),
    url(r'^multimedia/', include('multimedia.urls', namespace='multimedia', app_name='multimedia')),
    url(r'^admin/', admin.site.urls),
]
