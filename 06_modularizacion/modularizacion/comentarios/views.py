from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Comment

def test(request):
    return HttpResponse("Pruebas")

def create(request):
    #comment = Comment(name = 'Carlos', score = 5, comment="Comentario por defecto")
    #comment.save()
    comment = Comment.objects.create(name='Carlos2')
    return HttpResponse('Create')

def delete(request):
    #comment = Comment.objects.get(id = 1)
    #comment.delete()
    Comment.objects.filter(id=3).delete()
    return HttpResponse('Comentario Eliminado')