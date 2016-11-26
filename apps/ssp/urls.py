from django.conf.urls import url
from .views import *
from django.contrib.auth.views import login, logout_then_login

urlpatterns = [
	url(r'^$',index_view,name='index_view'),
	url(r'^listado_proyecto/$',listado_proyecto,name='listado_proyecto'),
	url(r'^buscar_proyecto/$',buscar_proyecto,name='buscar_proyecto'),
	url(r'^solicitud/$',solicitud,name='solicitud'),
	url(r'^curriculum/$',curriculum.as_view(),name='curriculum'),
	url(r'^login/$',login,{'template_name':'ssp/login.html'}, name='login'),
	url(r'^logout/$', logout_then_login, name='logout'),
	url(r'^detalle_empresa/(?P<slug>[-\w]+)/$',detalle_empresa.as_view(),name='detalle_empresa'),
	url(r'^detalle_proyecto/(?P<pk>[-\d]*)/$',detail_proyect.as_view(),name='detalle_proyecto'),
	url(r'^detalle_perfil/(?P<pk>[-\d]*)/$',detalle_perfil.as_view(),name='detalle_perfil'),
	url(r'^registroEstudiantes/$',registroEstudiantes.as_view(),name='registroEstudiantes'),
	url(r'^registroEmpresa/$',registroEmpresa.as_view(),name='registroEmpresa'),
	url(r'^register_proyecto/$',register_proyecto.as_view(),name='register_proyecto'),
	url(r'^proyectos_en_curso/$',proyecto_en_curso,name='proyectos_en_curso'),
	url(r'^update_proyecto_empresa_mostrar/(?P<pk>[-\w]+)/$',update_proyecto_empresa_mostrar.as_view(),name='update_proyecto_empresa_mostrar'),
	url(r'^update_proyecto_estudiante/(?P<pk>[-\w]+)/$',update_proyecto_estudiante.as_view(),name='update_proyecto_estudiante'),
	url(r'^update_proyecto_empresa/(?P<pk>[-\w]+)/$',update_proyecto_empresa.as_view(),name='update_proyecto_empresa'),
]