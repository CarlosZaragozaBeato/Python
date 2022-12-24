from django.http import HttpResponse
from django.shortcuts import render
from .forms import CommentForm,ContactForm

def form(request):
    commentForm = CommentForm({"name":"Carlos","url":"https://btm.com", "comment":"Comment one"})
    return render(request, 'form.html', {'comment_form':commentForm})    

def goal(request):
    if request.method != "POST":
        return HttpResponse("Metodo no Permitido")
    return HttpResponse(request.POST['name'])


def widget(request):
    if request.method == 'GET':
        form = ContactForm()
        return render(request, 'widget.html',{'form':form})
    if request.method == 'POST':
        form =  ContactForm(request.POST)
        if form.is_valid():
            return HttpResponse('Valido')
        else:
            return render(request, 'widget.html',{'form':form})