from django.core.management.base import BaseCommand
from myapp.models import Client

class Command(BaseCommand):
    help = "Create user."
    def handle(self, *args, **kwargs):
        client = Client(name='John', email='john@example.com', number_client='89997654321', address='qqwed.jhiygyu')
        client.save()
        self.stdout.write(f'{client}')