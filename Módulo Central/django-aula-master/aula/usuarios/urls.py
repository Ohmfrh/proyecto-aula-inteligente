from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url(r'^usuario/$', views.usuario, name='usuario'),
    url(r'^editar/$', views.editar, name='editar'),
]