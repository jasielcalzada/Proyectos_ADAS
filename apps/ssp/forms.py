from django import forms
from django.forms import ModelForm
from .models import Estudiante,Empresa
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EstudianteForm(UserCreationForm):
	nombre = forms.CharField(max_length=64)
	ncontrol = forms.SlugField()
	carreras = (('Ingenieria en sistemas computacionales','Ingenieria en sistemas computacionales'),('Ingenieria en TICS','Ingenieria en TICS'),('Ingenieria en informatica','Ingenieria en informatica'))
	carrera = forms.ChoiceField(choices=carreras,required=True,)
	
class EmpresaForm(UserCreationForm):
	nombre = forms.CharField(max_length=64)
	mail = forms.EmailField()
	phone = forms.IntegerField()
	rfc = forms.SlugField()