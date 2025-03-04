from django.shortcuts import render
from django.views.generic import TemplateView
from main_app.models import About, Project


# Create your views here.
from django.http import HttpResponse

class Home(TemplateView):
    template_name = 'main_app/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()
        return context

def about(request):
    return render(request, 'main_app/about.html')