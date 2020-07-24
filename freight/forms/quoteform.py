from django import forms
from freight.models.quotes import Quotes 

class QuoteForm(forms.ModelForm):
    def get_country():
        country=Quotes.get_countries()
        if country:
            return country
        else:
            raise forms.ValidationError("Contact Owner no Country found")

    name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your Name','style':'display:block;'}),label='')
    email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Your Email'}),label='')
    goods=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Goods','style':'display:block;'}),label='')
    c_type=forms.ChoiceField(choices=Quotes.types,label='Type')
    destination=forms.ChoiceField(choices=get_country(),label='Destination')
    origin=forms.ChoiceField(choices=get_country(),label='Origin')
    ctr_code=forms.ChoiceField(choices=Quotes.cnt_codes,label='Phone')
    phone=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your Phone'}),label='')
    q_message=forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Your Message...'}),label='')
    class Meta:
        model=Quotes
        fields="__all__"
