from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from models import Pages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def handler(request, recurso):
    if request.method == "GET":
        try:
            fila = Pages.objects.get(name=recurso)
            return HttpResponse(fila.page)
        except Pages.DoesNotExist:
            return HttpResponseNotFound('Pagina no encontrada: /%s.' % recurso)

    elif request.method == "PUT":
        new = Pages(name=recurso, page=request.body)
        new.save()
        return HttpResponse("Guardado")

    else:
        return HttpResponseNotFound("Error en el metodo")
