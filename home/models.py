# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Demandeur(models.Model):

    #__Demandeur_FIELDS__
    nom = models.CharField(max_length=255, null=True, blank=True)
    telephone = models.CharField(max_length=255, null=True, blank=True)
    service = models.CharField(max_length=255, null=True, blank=True)

    #__Demandeur_FIELDS__END

    class Meta:
        verbose_name        = _("Demandeur")
        verbose_name_plural = _("Demandeur")


class Admin(models.Model):

    #__Admin_FIELDS__

    #__Admin_FIELDS__END

    class Meta:
        verbose_name        = _("Admin")
        verbose_name_plural = _("Admin")



#__MODELS__END
