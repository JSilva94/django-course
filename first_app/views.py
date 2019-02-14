from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, WebPage, AccessRecord
# Create your views here.

def index(req):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}

    return render(req, 'first_app/index.html', context=date_dict)

def other(req):
    context_dict = {'text': 'hello world', 'number': 100}
    return render(req, 'first_app/other.html', context=context_dict)

def relative(req):
    return render(req, 'first_app/relative_url_templates.html')
