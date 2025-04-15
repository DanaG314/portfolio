from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'placeholder': 'Enter your email',
        'class': 'form-control',
    }))
    message = forms.CharField(label='', widget=forms.Textarea(attrs={
        'placeholder': 'Type a message',
        'class': 'form-control',
    }))