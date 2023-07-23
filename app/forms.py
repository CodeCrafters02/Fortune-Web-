from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    mobile = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(widget=forms.TimeInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Contact
        fields = '__all__'