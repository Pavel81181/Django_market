    # name = models.CharField(max_length=100)
    # description = models.TextField()
    # price = models.DecimalField(max_digits=8, decimal_places=2)
    # stock = models.DecimalField


from django.core.management.base import BaseCommand
from marketapp.models import Product

class Command(BaseCommand):
    help = "Create product."

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='client name')
        parser.add_argument("description", type=str, help="product description")
        parser.add_argument("price", type=float, help="product price")
        parser.add_argument("stock", type=float, help="product quantity")

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        description = kwargs.get('description')
        price = kwargs.get('price')
        stock = kwargs.get('stock')

        product = Product(name=name, description=description, price=price,  stock=stock)
        product.save()
        self.stdout.write(f'{product}')