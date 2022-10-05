'''Home views'''
from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail


def home(request):
    '''Home page view'''
    return render(request, "home/index.html")


def energy_saving(request):
    '''Energy Saving page view'''
    return render(request, "home/energy_saving.html")


def how_it_works(request):
    '''How it works page view'''
    return render(request, "home/how_it_works.html")


def service_life(request):
    '''How long it lasts page view'''
    return render(request, "home/service_life.html")


def contact(request):
    '''Contact page view'''
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['emailaddress']
        message = request.POST['message']

        print(message_name + message_email + message)

        send_mail('message from ' + message_name,
                  message + ' reply to this message ' + message_email,
                  message_email,
                  ['alvisenergysolutions@gmail.com'])
        messages.success(request,
                         'Email received. We will contact you shortly.')
        return render(request, "home/contact.html")
    else:
        return render(request, "home/contact.html")
