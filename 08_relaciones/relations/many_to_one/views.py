from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Reporter, Article
from datetime import date

def create(request):
    reporter = Reporter(first_name= "Carlos",last_name= "Zaragoza",email="crs@demo.com")
    reporter.save()
    article_1 = Article(headline ='lorem ipsum1',pub_date=date(2022,5,5,),reporter = reporter)    
    article_2 = Article(headline='lorem ipsum2',pub_date=date(2018,5,5,), reporter=reporter)    
    article_3 = Article(headline='lorem ipsum3',pub_date=date(2015,5,5,), reporter=reporter)    
    article_4 = Article(headline='lorem ipsum4',pub_date=date(2016,5,5,), reporter=reporter)    
    article_5 = Article(headline='lorem ipsu5',pub_date=date(2012,5,5,), reporter=reporter)    


    article_1.save()
    article_2.save()
    article_3.save()
    article_4.save()
    article_5.save()
    
    #result_1 = article_1.reporter.first_name
    #result_1 = reporter.article_set.filter(headline="lorem ipsum2")
    #result_1 = reporter.article_set.all()
    result_1 = reporter.article_set.count()
    return HttpResponse(result_1)