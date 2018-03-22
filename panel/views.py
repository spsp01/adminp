from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'panel/index.html'

class TableData(TemplateView):
    template_name = 'panel/datatable.html'