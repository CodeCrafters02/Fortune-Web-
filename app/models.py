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
