from django.shortcuts import render
from django.views.generic import (TemplateView,ListView,DeleteView,
                                DetailView,CreateView,UpdateView)
from django.urls import reverse_lazy
from . import models

class IndexView(TemplateView):
    template_name = 'index.html'

class SchoolListView(ListView):
    model = models.School

    # changes school_list to schools
    context_object_name = 'schools'

class SchoolDetailView(DetailView):
    model = models.School
    template_name = 'first_app/school_detail.html'

    # changes school to school_detail
    context_object_name = 'school_detail'

class SchoolCreateView(CreateView):
    model = models.School
    fields = ('name', 'principal', 'location')

class SchoolUpdateView(UpdateView):
    model = models.School
    fields = ('name', 'principal')

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('first_app:list')