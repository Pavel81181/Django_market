from django.core.management.base import  BaseCommand
from marketapp.models import Order

class Command(BaseCommand):
    help = "Get order by id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='id of order')      #pk - id

    def handle (self, *args, **kwargs):
        id_order = kwargs.get('pk')
        order = Order.objects.filter(pk=id_order).first()                            # поиск строки по id
        self.stdout.write(f'{order}')