from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.models import User 
from .models import Estudiante,Empresa,Proyecto,Curriculum
# Register your models here.
@admin.register(Estudiante)
class admin_estudiante(admin.ModelAdmin):
	list_display = ('ncontrol','nombre','carrera','categoria')

@admin.register(Empresa)
class admin_empresa(admin.ModelAdmin):
	list_display = ('rfc','nombre','mail','phone','categoria')

@admin.register(Proyecto)
class admin_proyecto(admin.ModelAdmin):
	list_display = ('id','nombre','descripcion','fecha_publicacion','perfil_proyecto','mostrar','categoria','selecionar','aprovado','empresa','estudiantess')
	
@admin.register(Curriculum)
class admin_proyecto(admin.ModelAdmin):
	#pass
	list_display = ('perfil','tecnologias','experiencia_profesional','get_idioma','fortaleza','done')

	def get_idioma(self,obj):
		lista = obj.idioma
		for i in lista:
			b = i
		return b
