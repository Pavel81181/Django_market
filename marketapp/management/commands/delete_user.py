from django.core.management.base import BaseCommand
from marketapp.models import User


class Command(BaseCommand):
    help = "delete User by id"

    def add_arguments(self, parser):

        parser.add_argument('pk', type=int, help='id of user')      #pk - id

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = User.objects.filter(pk=pk).first()                 #поиск строки по id

        if user is not None:
            user.delete()                                            #удаление найденной строки

        self.stdout.write(f'{user}')