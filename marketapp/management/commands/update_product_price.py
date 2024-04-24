from django.core.management.base import BaseCommand
from marketapp.models import Product


class Command(BaseCommand):
    help = "update product price by id product"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='id of products')  # pk - id
        parser.add_argument("price", type=float, help="price of product")

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        price = kwargs.get('price')
        product = Product.objects.filter(pk=pk).first()                  # поиск строки по id
        product.price = price
        product.save()                                                      # сохранение в БД
        self.stdout.write(f'{product}')