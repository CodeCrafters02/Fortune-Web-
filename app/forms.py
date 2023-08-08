from django import forms

from .models import Contact,Membership


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    mobile = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(widget=forms.TimeInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Contact
        fields = '__all__'


class MembershipForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    mobile = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    ABOUT_CHOICES = (
        ('...','...'),
        ('linkedin','LinkedIn'),
        ('google','Google'),
        ('facebook','Facebook'),
        ('instagram','Instagram'),
        ('twitter','Twitter'),
        ('youtube','YouTube'),

    )
    where_did_you_hear_about_us = forms.ChoiceField(choices=ABOUT_CHOICES,widget=forms.Select(attrs={'class': 'form-control'}))

    CONTACT_CHOICES = (
        ('...','...'),
        ('phone','Phone'),
        ('email','Email'),
        ('whatsapp','Whatsapp'),

    )
    preferred_way_to_contact = forms.ChoiceField(choices=CONTACT_CHOICES,widget=forms.Select(attrs={'class': 'form-control'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Membership
        fields = '__all__'