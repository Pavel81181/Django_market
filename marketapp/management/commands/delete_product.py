from django.core.management.base import BaseCommand
from marketapp.models import Product


class Command(BaseCommand):
    help = "delete product by id"

    def add_arguments(self, parser):

        parser.add_argument('pk', type=int, help='id of products')      #pk - id

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product = Product.objects.filter(pk=pk).first()                 #поиск строки по id

        if product is not None:
            product.delete()                                            #удаление найденной строки

        self.stdout.write(f'{product}')