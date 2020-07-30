from django.urls import path
from freight.controller import admin
from django.conf.urls import url,include

from freight.controller import index
from freight.controller import about
from freight.controller import services
from freight.controller import error
from freight.controller import contact
from freight.controller import quote
from freight.controller import terms

urlpatterns = [
    url(r'^admin',admin.admin,name="admin"),

    url(r'^$',index.index,name="index"),
    url(r'^about',about.about,name="about"),
    url(r'^services',services.services,name="services"),
    url(r'^error',error.error,name="error"),
    url(r'^contact',contact.contact,name="contact"),
    url(r'^quote',quote.quote,name="quote"),
    url(r'^terms',terms.terms,name="terms"),
]
