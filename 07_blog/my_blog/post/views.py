from django.shortcuts import render
from django.http import HttpResponse
from .models import Author,Entry

# Create your views here.

def queries(request):
    authors=Author.objects.all()
    filtered = Author.objects.filter(email='umanning@example.net')
    author = Author.objects.get(id=1)
    limit = Author.objects.all()[:10]
    offset = Author.objects.all()[5:10]
    orders = Author.objects.all().order_by('email') 
    
    """
    __lte: menor o igual
    __gte: mayor o igual
    
    __lt: menor que
    __gt: mayor que 
    
    __contains: contiene
    __exact: exacto
    """
    filtered_2 = Author.objects.filter(id__lte =15)
    contiene = Author.objects.filter(name__contains = "yes")
    
    
    
    return render(request, 'post/queries.html',{'authors':authors, 
                                                'filtered':filtered,
                                                'author':author,
                                                'limit':limit,
                                                'offset':offset,
                                                'orders':orders,
                                                'filtered_2':filtered_2,
                                                'contiene':contiene})

def update(request):
    author = Author.objects.get(id=1)
    author.name = 'carlos'
    author.email = 'crs@gmail.nett'
    author.save()
    return HttpResponse('Actuzalizada')