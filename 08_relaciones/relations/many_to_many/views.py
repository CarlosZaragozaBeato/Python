from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Publication
# Create your views here.



def create(request):
    """
    article1 = Article(headline = "article_1")
    article2 = Article(headline = "article_2")
    article3 = Article(headline = "article_3")
    
    article1.save()
    article2.save()
    article3.save()
    
    publication1 = Publication(title = "Title1")
    publication2 = Publication(title = "Title2")
    publication3 = Publication(title = "Title3")
    publication4 = Publication(title = "Title4")
    publication5 = Publication(title = "Title5")
    publication6 = Publication(title = "Title6")
    publication7 = Publication(title = "Title7")
    
    publication1.save()
    publication2.save()
    publication3.save()
    publication4.save()
    publication5.save()
    publication6.save()
    publication7.save()
    
    article1.publications.add(publication1)
    article1.publications.add(publication2)
    article1.publications.add(publication3)
    
    article2.publications.add(publication4)
    article2.publications.add(publication5)
    article2.publications.add(publication6)
    article3.publications.add(publication7)
    """
    
    pub = Publication.objects.get(id = 1)
    #result = article1.publications.all()
    result = pub.article_set.all()
    return HttpResponse(result)