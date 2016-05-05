from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^crear/$', views.crear, name='crear'),
    url('^servidor/$', views.servidor, name='servidor'),
    url('^editar/$', views.editar, name='editar'),
    url('^eliminar/$', views.eliminar, name='eliminar'),
]