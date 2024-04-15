from django.core.management.base import BaseCommand
from myapp.models import Client

class Command(BaseCommand):
    help = "get user."
    def handle(self, *args, **kwargs):
        client = Client.objects.all()
        self.stdout.write(f'{client}')