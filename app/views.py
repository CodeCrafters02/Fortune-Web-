from django.shortcuts import render,redirect
from .forms import ContactForm,MembershipForm
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
                ['cbn@fortuneedu.in'],  # Replace with the admin's email address
                fail_silently=False,
            )
            
            return redirect('home')
    else:
        form = ContactForm()

    context = {
        'form': form
    }
    return render(request, 'index.html', context)


def membership_form(request):
    if request.method == 'POST':
        form = MembershipForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            where_did_you_hear_about_us = form.cleaned_data['where_did_you_hear_about_us']
            preferred_way_to_contact = form.cleaned_data['preferred_way_to_contact']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Sending the email to the admin
            send_mail(
                subject,
                
                f"Greetings for the Day!!\nPlease do find the new Leads below.. \n\nFirst Name: {first_name}\nLast Name: {last_name}\nEmail: {email}\nMobile: {mobile}\nWhere did you hear about us: {where_did_you_hear_about_us}\nPreferred way to Contact:{preferred_way_to_contact}\nMessage:{message}\n\nThanks & Regards",
                'Code Crafters <servicescc.002@gmail.com>',  # Replace with the sender's email address
                ['cbn@fortuneedu.in'],  # Replace with the admin's email address
                fail_silently=False,
            )
            
            return redirect('home')
    else:
        form = MembershipForm()

    context = {
        'form': form
    }
    return render(request, 'membership_form.html',context)