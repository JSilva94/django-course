from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, WebPage, AccessRecord
# Create your views here.

def index(req):
   

    return render(req, '/index.html')