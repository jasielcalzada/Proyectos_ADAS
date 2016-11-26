from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.views.generic import FormView, CreateView, ListView,DetailView,UpdateView,DeleteView
from .forms import EstudianteForm, EmpresaForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from .models import Estudiante, Empresa, Proyecto, Curriculum
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger
from django.contrib.auth.models import User
# Create your views here.

def index_view(request):
	return render(request,'ssp/index.html')

class registroEstudiantes(FormView):
	template_name = 'ssp/registroEstudiante.html'
	form_class = EstudianteForm
	success_url = reverse_lazy('index_view')

	def form_valid(self,form):
		user = form.save()
		p = Estudiante()
		p.user_perfil = user
		p.nombre = form.cleaned_data['nombre']
		p.ncontrol = form.cleaned_data['ncontrol']
		p.carrera = form.cleaned_data['carrera']
		p.save()
		return super(registroEstudiantes,self).form_valid(form)

class registroEmpresa(FormView):
	template_name = 'ssp/registroEmpresa.html'
	form_class = EmpresaForm
	success_url = reverse_lazy('index_view')

	def form_valid(self,form):
		user = form.save()
		p = Empresa()
		p.user_perfil = user
		p.nombre = form.cleaned_data['nombre']
		p.mail = form.cleaned_data['mail']
		p.phone = form.cleaned_data['phone']
		p.rfc = form.cleaned_data['rfc']
		p.save()
		return super(registroEmpresa,self).form_valid(form)

class register_proyecto(CreateView):
	template_name='ssp/ingresar_proyecto.html'
	model = Proyecto
	fields=['nombre','descripcion','fecha_publicacion','perfil_proyecto','mostrar','categoria','empresa']
	success_url=reverse_lazy('index_view')

def listado_proyecto(request):
	current_user = request.user.empresas.rfc
	pro = Proyecto.objects.filter(empresa = current_user)
	ctx={"pro":pro}
	return render(request,'ssp/listado_proyectos.html',ctx)	

class update_proyecto_empresa_mostrar(UpdateView):
	model = Proyecto
	fields = ['mostrar']
	template_name = 'ssp/updateMostrarProyecto.html'
	success_url = reverse_lazy('index_view')

class update_proyecto_estudiante(UpdateView):
	model = Proyecto
	fields = ['estudiantess','selecionar']
	template_name = 'ssp/actualizarproestu.html'
	success_url = reverse_lazy('index_view')

def buscar_proyecto(request):
	if request.POST:
		data = request.POST['campo']
		p =Proyecto.objects.filter(categoria =data)
		empresas = Empresa.objects.all()
		ctx = {'objects':p,'empresas':empresas}
		print ctx
	else:
		ctx={'mensaje':'No hay datos'}
	return render(request,'ssp/buscar_proyecto.html',ctx)

class detalle_empresa(DetailView):
	template_name = 'ssp/detalle_empresa.html'
	slug_field = 'rfc'
	model = Empresa	

class detail_proyect(DetailView):
	template_name = 'ssp/detalleProyecto.html'
	model = Proyecto

def proyecto_en_curso(request):
	current_user = request.user.profile.ncontrol
	p = Estudiante.objects.all()
	c = Proyecto.objects.filter(estudiantess = current_user)
	print c
	ctx={"est":p,"pro":c}
	return render(request,'ssp/pro_encurso.html',ctx)

class curriculum(CreateView):
	template_name='ssp/curriculum.html'
	model = Curriculum
	fields=['tecnologias','experiencia_profesional','idioma','fortaleza','done']
	success_url=reverse_lazy('index_view')
	def post(self, request, *args, **kwargs): 
		flag=False 
		c = Curriculum()
		c.perfil = request.user
		c.tecnologias=request.POST['tecnologias']
		c.experiencia_profesional=request.POST['experiencia_profesional']
		c.idioma=request.POST['idioma']       
		c.fortaleza=request.POST['fortaleza']
		c.done = True
		c.save()
		flag=True
		per = Curriculum.objects.all()
		ctx = {'flag':flag,'per':per}

		return render(request, 'ssp/curriculum.html',ctx)

def solicitud(request):
	current_user = request.user.empresas.rfc
	proyectos = Proyecto.objects.filter(empresa = current_user)
	curriculums = Curriculum.objects.all()
	empresas = Empresa.objects.all()
	ctx = {'proyectos':proyectos,'curriculums':curriculums,'empresas':empresas}
	return render(request,'ssp/solicitud.html',ctx)

class detalle_perfil(DetailView):
	template_name = 'ssp/detalle_perfil.html'
	model = Curriculum

class update_proyecto_empresa(UpdateView):
	model = Proyecto
	fields = ['aprovado','selecionar']
	template_name = 'ssp/actualizarproempresa.html'
	success_url = reverse_lazy('index_view')
		