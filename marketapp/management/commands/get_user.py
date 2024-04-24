from django.core.management.base import  BaseCommand
from marketapp.models import User

class Command(BaseCommand):
    help = "Get user by id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='id of user')      #pk - id

    def handle (self, *args, **kwargs):
        id_user = kwargs.get('pk')
        user = User.objects.filter(pk=id_user).first()                            # поиск строки по id
        self.stdout.write(f'{user}')