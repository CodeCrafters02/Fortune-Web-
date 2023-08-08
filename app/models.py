from django.db import models



class Contact(models.Model):
    name = models.CharField(max_length=100, null=True)
    mobile = models.CharField(max_length=20,null=True)
    email = models.CharField(max_length=50,null=True)
    subject = models.CharField(max_length=100,null=True)
    message = models.TextField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True,null=True)
    
    
    def __str__(self):
        return self.subject
    

class Membership(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    mobile = models.CharField(max_length=20,null=True)
    email = models.CharField(max_length=50,null=True)

    ABOUT_CHOICES = (
        ('linkedin','LinkedIn'),
        ('google','Google'),
        ('facebook','Facebook'),
        ('instagram','Instagram'),
        ('twitter','Twitter'),
        ('youtube','YouTube'),

    )
    where_did_you_hear_about_us = models.CharField(max_length=50,choices=ABOUT_CHOICES,null=True)

    CONTACT_CHOICES = (
        ('phone','Phone'),
        ('email','Email'),
        ('whatsapp','Whatsapp'),

    )
    preferred_way_to_contact = models.CharField(max_length=50,choices=CONTACT_CHOICES, null=True)
    subject = models.CharField(max_length=100,null=True)
    message = models.TextField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True,null=True)
    
    
    def __str__(self):
        return self.first_name
