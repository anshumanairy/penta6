from django import forms
from freight.models.quotes import Quotes

class QuoteForm(forms.ModelForm):
    def get_country():
        country=Quotes.get_countries()
        if country:
            return country
        else:
            raise forms.ValidationError("Contact Owner no Country found")

    name=forms.CharField(widget=forms.TextInput(attrs={'id':'form1','class':'form-control','placeholder':'Enter Your Name','style':'display:block;background:rgba(0,0,0,0.8);border-radius:5px;color:white;'}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Email','style':'background:rgba(0,0,0,0.8);border-radius:5px;color:white;'}))
    goods=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Goods','style':'background:rgba(0,0,0,0.8);border-radius:5px;color:white;'}))
    quantity=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Quantity','style':'background:rgba(0,0,0,0.8);border-radius:5px;color:white;'}))
    c_type=forms.ChoiceField(choices=Quotes.types,label='Type',widget=forms.Select(attrs={'class':'form-control','placeholder':'Type','style':'background:rgba(0,0,0,0.8);border-radius:5px;border-color:black;color:gray;width:100%;'}))
    try:
        destination=forms.ChoiceField(choices=get_country(),label='Destination',widget=forms.Select(attrs={'class':'form-control','placeholder':'Destination','style':'background:rgba(0,0,0,0.8);border-color:black;border-radius:5px;color:gray;width:100%;'}))
    except:
        pass
    destination_address=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Destination Address','style':'resize:none;background:rgba(0,0,0,0.8);border-radius:5px;color:white;'}))
    destination_pincode=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Destination Pin','style':'background:rgba(0,0,0,0.8);border-radius:5px;color:white;'}))
    try:
        origin=forms.ChoiceField(choices=get_country(),label='Origin',widget=forms.Select(attrs={'class':'form-control','placeholder':'Origin','style':'background:rgba(0,0,0,0.8);border-radius:5px;border-color:black;color:gray;width:100%;'}))
    except:
        pass
    origin_address=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Source Address','style':'resize:none;background:rgba(0,0,0,0.8);border-radius:5px;color:white;'}))
    origin_pincode=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Source Pin','style':'background:rgba(0,0,0,0.8);border-radius:5px;color:white;'}))
    ctr_code=forms.ChoiceField(choices=Quotes.cnt_codes,label='Country Code',widget=forms.Select(attrs={'class':'form-control','placeholder':'Country Code','style':'background:rgba(0,0,0,0.8);border-radius:5px;border-color:black;color:gray;width:100%;'}))
    phone=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your Phone','style':'background:rgba(0,0,0,0.8);border-radius:5px;color:white;'}))
    q_message=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Your Message...','style':'resize:none;background:rgba(0,0,0,0.8);border-radius:5px;color:white;'}),label='Message')
    class Meta:
        model=Quotes
        fields="__all__"
