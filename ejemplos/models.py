from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    id=models.AutoField(primary_key=True)
    phone=models.CharField(max_length=50)
    direction=models.CharField(max_length=200)
    email=models.CharField(max_length=50,null=True)
    fb=models.CharField(max_length=50,null=True)
    google=models.CharField(max_length=50,null=True)
    rif=models.CharField(max_length=50)
    localphone=models.CharField(max_length=50,null=True)
    reference=models.CharField(max_length=200,null=True)
    class Meta:
        verbose_name_plural = "Perfil de Usuario"
