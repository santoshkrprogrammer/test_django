from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Permission

@receiver(post_save, sender=Permission)
def post_save(sender, instance: Permission, **kwargs):
   print("hello from test signal")