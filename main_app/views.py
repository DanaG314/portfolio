from django.shortcuts import render
from django.core.mail import send_mail
from .forms import EmailForm
from django.views.generic import TemplateView
from main_app.models import About, Project




class Home(TemplateView):
    template_name = 'main_app/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()

        projects = Project.objects.all()
        context['simon']= projects.filter(title='Simon!').first()
        context['binge_buddy']= projects.filter(title='Binge Buddy').first()
        context['legodex']= projects.filter(title='LegoDex').first()
        context['shelf_space']= projects.filter(title='Shelf Space').first()
        
        return context

def about(request):
    return render(request, 'main_app/about.html')

# def email_view(request):
#     if request.method == 'POST':
#         form = EmailForm(request.POST)
#         if form.is_valid():
#             user_email = form.cleaned_data['email']

#             send_mail(

#             )


# def projects_page(request):
#     projects = Project.objects.all()
#     context = {
#         'simon': projects.filter(title='Simon!').first(),
#         'binge_buddy': projects.filter(title='Binge Buddy').first(),
#         'legodex': projects.filter(title='LegoDex').first(),
#         'shelf_space': projects.filter(title='Shelf Space').first(),
#     }
#     return render(request, 'main_app/projects.html', context)