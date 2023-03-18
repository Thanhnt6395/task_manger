from django.db.models.signals import post_save, pre_delete
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.dispatch import receiver

from ..common.send_mail import send_mail_active
 
 
User = get_user_model()

@receiver(post_save, sender=Token, dispatch_uid="register_activity")
def register(sender, instance, created, **kwargs):
    if created:
        # token = Token.objects.get(user=instance)
        send_mail_active(instance)