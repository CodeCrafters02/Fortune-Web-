from django.shortcuts import render,redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Sending the email to the admin
            send_mail(
                subject,
                f"Name: {name}\nMobile: {mobile}\nEmail: {email}\nMessage: {message}",
                'Code Crafters <servicescc.002@gmail.com>',  # Replace with the sender's email address
                ['iamrenjith17@gmail.com'],  # Replace with the admin's email address
                fail_silently=False,
            )
            
            return redirect('home')
    else:
        form = ContactForm()

    context = {
        'form': form
    }
    return render(request, 'index.html', context)
