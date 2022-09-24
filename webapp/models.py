from ctypes import addressof
from operator import iconcat
from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=30)
    ic = models.CharField(max_length=15)
    status_choices = [
        ('POSITIVE', 'Positive'),
        ('NEGATIVE', 'Negative')
    ]
    status = models.CharField(max_length=10, choices=status_choices)    
    date = models.DateTimeField(auto_now_add=True)
    street_address = models.CharField(max_length=40)
    postcode = models.IntegerField()
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)


    def __str__(self):
        return self.name