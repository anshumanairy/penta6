from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget= forms.TextInput
                           (attrs={'placeholder':'Eg.John Mathew','style': 'width:600px;border-radius:5px;'}))
    email = forms.EmailField( widget= forms.EmailInput
                           (attrs={'placeholder':'Eg. example@example.com','style': 'width:600px;border-radius:5px;'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message...','style':'width:600px;border-radius:5px;resize:none'}))
