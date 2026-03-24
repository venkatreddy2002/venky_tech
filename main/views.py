from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for reaching out! Your message has been sent.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'main/contact.html', {'form': form})

def payment(request):
    return render(request, 'main/payment.html')
