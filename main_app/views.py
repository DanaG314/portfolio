from django.shortcuts import render, redirect
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
        
        context['form'] = EmailForm()

        return context

    def post(self, request, *args, **kwargs):
        form = EmailForm(request.POST)
        context = self.get_context_data()

        if form.is_valid():
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']  # ⬅️ Get the message

            send_mail(
                subject='New Contact Form Submission',
                message=f'Email: {email}\n\nMessage:\n{message}',  # ⬅️ Include message
                from_email=email,
                recipient_list=['danagabay@msn.com'],
                fail_silently=False,
            )

            context['success'] = True
            context['form'] = EmailForm()
        else:
            context['form'] = form

        return self.render_to_response(context)

