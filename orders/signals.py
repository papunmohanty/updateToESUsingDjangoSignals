from orders.search_indexes.orders import OrderDocument
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from orders.models import Order


@receiver(post_save, sender=Order)
def index_order(sender, instance, created, **kwargs):
    if not created:
        # Updated existing order in Elasticsearch
        order = OrderDocument.get(id=instance.pk)
        order.order_number = instance.order_number
        order.customer_name = instance.customer_name
        order.total_amount = instance.total_amount
        order.save()
    else:
        # Index new order in Elasticsearch
        order = OrderDocument(
            meta={'id': instance.pk},
            order_number=instance.order_number,
            customer_name=instance.customer_name,
            total_amount=instance.total_amount
        )
        order.save()


@receiver(post_delete, sender=Order)
def delete_order(sender, instance, **kwargs):
    # Delete order from Elasticsearch
    order = OrderDocument.get(id=instance.pk)
    order.delete()
