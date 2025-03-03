from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
from django.http import HttpResponse

class Home(TemplateView):
    template_name = 'main_app/home.html'

def about(request):
    return render(request, 'main_app/about.html')