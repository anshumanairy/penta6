from django.db import models

class Country(models.Model):
    c_code=models.CharField(max_length=10)
    c_Name=models.CharField(max_length=50)

class Quotes(models.Model):
    types = (
    ('','Select an option'),
    ('L','Land'),
    ('A','Air'),
    ('O','Ocean')
    )
    cnt_codes=[
        ('','Select an option'),
        ('+1','USA (+1)'),
        ('+91','India (+91)')
    ]
    name=models.CharField(max_length=50)
    email=models.EmailField()
    goods=models.CharField(max_length=100)
    c_type=models.CharField(max_length=10,choices=types)
    destination=models.CharField(max_length=50)
    origin=models.CharField(max_length=50)
    ctr_code=models.CharField(max_length=10)
    phone=models.CharField(max_length=30)
    q_message=models.TextField(max_length=400)

    @staticmethod
    def get_countries():
        countries = Country.objects.all()
        t=[]
        for i in countries:
            a,b=i.c_code,i.c_Name
            t.append((a,b))
        t.sort(key=lambda x: x[1])
        return t