from django.http import HttpResponse

def saludo(request):
    return HttpResponse('Hello World')


def despedida(request):
    return HttpResponse('Hasta Luego')

def adulto(request,edad):
    if edad>=18:
        return HttpResponse("Es adulto")
    else:
        return HttpResponse("No es adulto")