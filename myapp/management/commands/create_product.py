from django.core.management.base import BaseCommand
from myapp.models import Product

class Command(BaseCommand):
    help = "Create product."
    def handle(self, *args, **kwargs):
        product = Product(name='product1', description='jvjyk.hblhnbn;jlvcfvgbhnjmkljnhbgv', price='321', quantity=3)
        product.save()
        self.stdout.write(f'{product}')