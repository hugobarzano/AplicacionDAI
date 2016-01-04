from django.http import HttpResponse
from django.shortcuts import render
from bares_y_tapas.models import *

def index(request):
	#contexto para enviar al motor de plantillas
	top_bares = Bar.objects.order_by('-visitas')[:5]
	top_tapas = Tapa.objects.order_by('-megusta')[:5]
	print top_tapas
	contexto = {'Bares': top_bares, 'Tapas': top_tapas}
	#Renderizamos la respuesta para el cliente
	return render(request, 'bares_y_tapas/index.html', contexto)

def todos(request):
	#contexto para enviar al motor de plantillas
	bares = Bar.objects.all()
	contexto = {'Bares': bares}
	#Renderizamos la respuesta para el cliente
	return render(request, 'bares_y_tapas/todos.html', contexto)

def about(request):
	return render(request, 'bares_y_tapas/about.html')

def details(request,nombre_bar):
	bar_detalle = Bar.objects.get(nombre=nombre_bar)
	#print bar_detalle
	#contexto ={'Bar': bar_detalle}
	#lista_tapas=Tapa.objects.order_by('-megusta')[:5]
	lista_tapas=Tapa.objects.filter(bar=bar_detalle)
	print lista_tapas
	contexto={ 'Bar': bar_detalle, 'Tapas' : lista_tapas}
	#print contexto
	return render(request, 'bares_y_tapas/details.html', contexto)

def bar(request, bar_nombre_slug):
	contexto = {}
	try:
		bar = Bar.objects.get(slug=bar_nombre_slug)
		contexto['bar_nombre'] = bar.nombre

		tapas = Tapa.objects.filter(bar=bar)
		contexto['tapas'] = tapas
		contexto['bar']=bar
	except Bar.DoesNotExist:
		pass

	return render(request,'bares_y_tapas/bar.html', contexto)
