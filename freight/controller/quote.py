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
from freight.forms.quoteform import QuoteForm
from freight.models.quotes import Country
from django.contrib import messages


def quote(request):
    form=QuoteForm(request.POST or None)
    context={"form":form}
    if form.is_valid():
        obj=form.save()
        print(obj)
        messages.add_message(request, messages.SUCCESS, 'We will Contact You Soon!!')
        return redirect('/quote')
    return render(request,'quote.html/',context)