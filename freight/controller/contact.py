from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,authenticate,logout,get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView
from django.template.response import TemplateResponse
from django.contrib.auth.hashers import check_password
import base64
import hashlib
import hmac
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.utils.timezone import utc
from django.utils import timezone
from freight.forms.contactform import ContactForm
from django.core.mail import send_mail
from django.contrib import messages


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']
            message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
            send_mail('New Enquiry', message, sender_email, ['cs@pentasixbright.com'], fail_silently=False)
            messages.add_message(request, messages.SUCCESS, 'Thanks for your feedback!!')
            # form = ContactForm()
            # return render(request, 'contact.html', {'form': form})
            # return render(request, 'index.html')
            print("Send")
            return redirect("contact")
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

# def contact(request):
#     return render(request,'contact.html/',{})
