from django.shortcuts import render
from django.views.generic import TemplateView

def func_templates(request):
    return render(request, 'second_task/func_templates.html')

class ClassTemplates(TemplateView):
    template_name = 'second_task/class_templates.html'

