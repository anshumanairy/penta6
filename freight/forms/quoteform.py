from django import forms
from freight.models.quotes import Quotes 

class QuoteForm(forms.ModelForm):
    def get_country():
        country=Quotes.get_countries()
        if country:
            return country
        else:
            raise forms.ValidationError("Contact Owner no Country found")

    name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your Name','style':'display:block;'}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Your Email'}))
    goods=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Goods'}))
    quantity=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Quantity'}))
    c_type=forms.ChoiceField(choices=Quotes.types,label='Type')
    destination=forms.ChoiceField(choices=get_country(),label='Destination')
    destination_address=forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Enter Destination Address'}))
    destination_pincode=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Enter Destination Pin'}))
    origin=forms.ChoiceField(choices=get_country(),label='Origin')
    origin_address=forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Enter Source Address'}))
    origin_pincode=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Enter Source Pin'}))
    ctr_code=forms.ChoiceField(choices=Quotes.cnt_codes,label='Country Code')
    phone=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your Phone'}))
    q_message=forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Your Message...'}),label='Message')
    class Meta:
        model=Quotes
        fields="__all__"
