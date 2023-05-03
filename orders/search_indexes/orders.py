# from elasticsearch_dsl import Document, Text, Integer, Float
from django_elasticsearch_dsl import Document, Text, Float
from django_elasticsearch_dsl.registries import registry

from orders.models import Order


@registry.register_document
class OrderDocument(Document):
    class Index:
        name = 'orders'

    class Django:
        model = Order
        fields = [
            'order_number',
            'customer_name',
            'total_amount',
        ]
