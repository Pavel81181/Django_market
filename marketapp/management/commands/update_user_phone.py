from django.core.management.base import BaseCommand
from marketapp.models import User


class Command(BaseCommand):
    help = "update user's phone  by user's id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='user id')  # pk - id
        parser.add_argument("phone", type=str, help="user phone")

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        phone = kwargs.get('phone')
        user = User.objects.filter(pk=pk).first()                  # поиск строки по id
        user.phone = phone
        user.save()                                                      # сохранение в БД
        self.stdout.write(f'{user}')