from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext as _
from django.db.models.signals import post_save
from django.dispatch import receiver

from .manager import CustomUserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.TextField(_("first name"), default=None)
    last_name = models.TextField(_("last name"), default=None)
    username = models.TextField(_("username"), default=None)
    is_staff = models.BooleanField(_("admin"), default=False)
    is_active = models.BooleanField(_("active"), default=False)
    create_at = models.DateField(_("created at"), auto_now=True)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    class Meta:
        db_table = 'Users'
        
    def __str__(self):
        return self.email