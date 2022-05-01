from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from .models import *
from .forms import *

# Create your views here.

def inicio(request):
	return render(request, "AppFulana/inicio.html")

def blog(request):
	if request.method == 'POST':
		miFormulario = PosteosForm(request.POST)
		print(miFormulario)
		if miFormulario.is_valid:
			informacion = miFormulario.cleaned_data
			posteo = Posteos(titulo=informacion['titulo'], post=informacion['contanos'])
			posteo.save()
			return render(request, "AppFulana/inicio.html")
	else:
		miFormulario = PosteosForm()

	return render(request, "AppFulana/blog.html",{"miFormulario":miFormulario})

def lenguajes(request):
	if request.method == 'POST':
		miFormulario2 = LenguajeForm(request.POST)
		print(miFormulario2)
		if miFormulario2.is_valid:
			informacion = miFormulario2.cleaned_data
			lenguaje = Lenguaje(lenguaje=informacion['lenguaje'], review=informacion['review'])
			lenguaje.save()
			return render(request, "AppFulana/inicio.html")
	else:
		miFormulario2 = LenguajeForm()

	return render(request, "AppFulana/lenguajes.html",{"miFormulario2":miFormulario2})

def instituto(request):
	if request.method == 'POST':
		miFormulario3 = InstitutoForm(request.POST)
		print(miFormulario3)
		if miFormulario3.is_valid:
			informacion = miFormulario3.cleaned_data
			instituto = Institutos(instituto=informacion['instituto'], review=informacion['review'])
			instituto.save()
			return render(request, "AppFulana/inicio.html")
	else:
		miFormulario3 = InstitutoForm()
	return render(request, "AppFulana/institutos.html",{"miFormulario3":miFormulario3})

def buscar(request):
	if request.GET['lenguaje']:
		lenguaje = request.GET['lenguaje']
		review = Lenguaje.objects.filter(lenguaje__icontains=lenguaje)
		return render (request, "AppFulana/buscar.html", {"lenguaje":lenguaje, "review":review})
	else:
		respuesta = "no enviaste datos"

	return HttpResponse(respuesta)

def acerca(request):
	return render(request, "AppFulana/acerca.html")