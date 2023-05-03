from django.core.management.base import BaseCommand
# from elasticsearch_dsl import Index
from django_elasticsearch_dsl import Index
from orders.search_indexes.orders import OrderDocument


class Command(BaseCommand):
    help = "Create Elasticsearch Indexes for the app"

    def handle(self, *args, **kwargs):
        help = 'Creates Elasticsearch indexes for the app'

    def handle(self, *args, **options):
        # Check if Elasticsearch index for OrderDocument exists
        index_name = OrderDocument._index._name
        if Index(index_name).exists():
            self.stdout.write(self.style.SUCCESS(f'Index "{index_name}" already exists.'))
            return

        # Create Elasticsearch index for OrderDocument
        OrderDocument.init()

        self.stdout.write(self.style.SUCCESS(f'Index "{index_name}" created successfully.'))