from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('^nuevo/$', views.nuevo, name='nuevo'),
    url('^editar/$', views.editar, name='editar'),
    url('^identificar/$', views.identificar, name='identificar'),
    url('^borrar/$', views.borrar, name='borrar'),
]