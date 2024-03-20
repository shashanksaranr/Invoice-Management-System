# mini/signals.py
from django.db.models.signals import post_save, post_delete,post_migrate
from django.dispatch import receiver
from .models import Invoice

@receiver(post_save, sender=Invoice)
def post_save_invoice(sender, instance, created, **kwargs):
    if created:
        print(f'Invoice {instance.invoice_id} created successfully!')
    else:
        print(f'Invoice {instance.invoice_id} updated successfully!')


@receiver(post_delete, sender=Invoice)
def post_delete_invoice(sender, instance, **kwargs):
    
    print(f'Invoice {instance.invoice_id} deleted successfully!')

