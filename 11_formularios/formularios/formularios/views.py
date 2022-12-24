
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def get_form(request):
    return render(request, 'form.html',{})

def get_goal(request):
    if request.method != 'GET':
        return HttpResponse("ERROR")
    
    name = request.GET['name']
    message = request.GET['cometario']
    return render(request, 'success.html',{'name':name,'message':message})


def post_form(request):
    return render(request, 'post_form.html',{})

def post_goal(request):

    if request.method != 'POST':
        return HttpResponse("ERROR")
    
    info = request.POST['info']
    
    return render(request, 'post_success.html',{'info':info})