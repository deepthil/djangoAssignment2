from django.shortcuts import render
import operator
from django.http import HttpResponse

def home(requests):
     return render(requests,'wcount/home.html')


def count(requests):
    mytext=requests.GET[ 'fulltext' ] 
    wcount=len(mytext.split())
    return render(requests, 'wcount/count.html',{'mycount':wcount})
