from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from multiselectfield import MultiSelectField
# Create your models here.
class Empresa(models.Model):
	user_perfil = models.OneToOneField(User,related_name='empresas')
	nombre = models.CharField(max_length=64)
	mail = models.EmailField()
	phone= models.IntegerField()
	rfc = models.SlugField(primary_key=True)
	categoria=models.CharField(max_length=10, default="empresa" , null=True)

	def __unicode__(self):
		return '%s'%(self.rfc)

class Estudiante(models.Model):
	user_perfil = models.OneToOneField(User,related_name="profile")
	nombre = models.CharField(max_length=64)
	ncontrol = models.SlugField(primary_key=True)
	carreras = (('Ingenieria en sistemas computacionales','Ingenieria en sistemas computacionales'),('Ingenieria en TICS','Ingenieria en TICS'),('Ingenieria en informatica','Ingenieria en informatica'))
	carrera = models.CharField(max_length=64,choices=carreras, default="No")
	categoria=models.CharField(max_length=10, default="estudiante" , null=True)


	def __unicode__(self):
		return '%s'%(self.ncontrol)

	#def get_proyecto(self):
	#	return "\n".join([p.nombre for p in self.proyect.all()])

class Proyecto(models.Model):
	nombre = models.SlugField(max_length=64,blank=False)
	descripcion = models.CharField(max_length=240)
	fecha_publicacion = models.DateField()
	perfil_proyecto = models.TextField(max_length=64)
	mostrar = models.BooleanField(default=False)
	c = (('programacion modular','programacion modular'),('programacion WEB','programacion WEB'),('redes de compuradora','redes de computadora'),('administracion de base de datos','administracion de base de datos'),('prueva','prueva'))
	categoria = models.CharField(max_length=124,choices= c ,default=False)
	selecionar = models.BooleanField(default=False)
	respuesta = (('aprovado','aprovado'),('rechasado','rechasado'),('en proceso','en proceso'))
	aprovado = models.CharField(max_length=44,choices=respuesta,default="en proceso")
	empresa = models.ForeignKey(Empresa,related_name="em")
	estudiantess = models.ForeignKey(Estudiante,null=True,blank=True)

	def __unicode__(self):
		return '%s %s %s %s'%(self.id,self.estudiantess,self.aprovado,self.estudiantess)

class Curriculum(models.Model):
	perfil = models.OneToOneField(User,related_name="more")
	tecnologias = models.TextField(max_length=500)
	experiencia_profesional = models.TextField(max_length=1000)
	MY_CHOICES =  (('espanol','espanol'),
               	   ('ingles','ingles'),
                   ('japones','japones'),
                   ('ruso', 'ruso'),
                   ('aleman','aleman'))
	idioma = MultiSelectField(choices=MY_CHOICES, max_choices=5,max_length=100)
	c = (('programacion modular','programacion modular'),('programacion WEB','programacion WEB'),('redes de compuradora','redes de computadora'),('administracion de base de datos','administracion de base de datos'))
	fortaleza = models.CharField(max_length=64,choices=c)
	done = models.BooleanField(default=False)

	def __unicode__(self):
		return '%s'%(self.id)
	def __str__(self):
		return '%s'%(self.id)



	

