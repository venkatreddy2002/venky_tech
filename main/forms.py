from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone_number', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your email address'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Your phone number (optional)'}),
            'subject': forms.TextInput(attrs={'placeholder': 'What is this regarding?'}),
            'message': forms.Textarea(attrs={'placeholder': 'How can we help you?', 'rows': 5}),
        }
