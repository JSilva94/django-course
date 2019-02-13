from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, WebPage, AccessRecord
from . import forms

# Create your views here.

def form_name_view(req):
    form = forms.FormName()

    if(req.method == 'POST'):
            form = forms.FormName(req.POST)
            if form.is_valid():
                print('VALIDATION SUCCESS')
                print('name ' + form.cleaned_data['name'])
                print('email ' + form.cleaned_data['email'])
                print('text ' + form.cleaned_data['text'])

    return render(req, 'first_app/forms.html', context={'form': form})

def index(req):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}

    return render(req, 'first_app/index.html', context=date_dict)

