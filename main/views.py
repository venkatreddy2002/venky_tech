from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_msg = form.save()
            
            # Send Email
            subject = f"Contact Form: {contact_msg.subject or 'New Message'}"
            message = (
                f"New contact form submission:\n\n"
                f"Name: {contact_msg.name}\n"
                f"Email: {contact_msg.email}\n"
                f"Phone: {contact_msg.phone_number or 'N/A'}\n"
                f"Subject: {contact_msg.subject or 'N/A'}\n\n"
                f"Message:\n{contact_msg.message}"
            )
            
            # Send to the admin email defined in settings
            recipient_list = [settings.CONTACT_RECIPIENT_EMAIL] 
            
            try:
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list, fail_silently=False)
                success_msg = 'Thank you! Your message has been sent successfully.'
                
                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    from django.http import JsonResponse
                    return JsonResponse({'status': 'success', 'message': success_msg})
                
                messages.success(request, success_msg)
            except Exception as e:
                import traceback
                print(f"EMAIL SEND ERROR: {str(e)}")
                traceback.print_exc()
                
                error_msg = 'There was an error sending your message. Please check your SMTP credentials.'
                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    from django.http import JsonResponse
                    return JsonResponse({'status': 'error', 'message': error_msg}, status=500)
                
                messages.error(request, error_msg)
                
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'main/contact.html', {'form': form})

def payment(request):
    return render(request, 'main/payment.html')
