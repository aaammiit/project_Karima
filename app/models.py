from django.db import models
from django import forms

# Create your models here.

class UFrm(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    age=models.IntegerField()
    phone=models.CharField(max_length=100)
    address=models.CharField(max_length=100)


class UserForm(forms.ModelForm):
    class Meta:
        model=UFrm
        fields='__all__'