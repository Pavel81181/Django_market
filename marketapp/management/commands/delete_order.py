from django.core.management.base import BaseCommand
from marketapp.models import Order


class Command(BaseCommand):
    help = "delete Order by id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='id of order')      #pk - id

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        order = Order.objects.filter(pk=pk).first()                 #поиск строки по id

        if order is not None:
            order.delete()                                            #удаление найденной строки

        self.stdout.write(f'{order}')