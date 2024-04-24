from django.core.management.base import BaseCommand
from marketapp.models import User

class Command(BaseCommand):
    help = "Create user."

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='client name')
        parser.add_argument("email", type=str, help="client email")
        parser.add_argument("phone", type=str, help="client phone_number")
        parser.add_argument("address", type=str, help="client adress")

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        email = kwargs.get('email')
        phone = kwargs.get('phone')
        address = kwargs.get('address')

        user = User(name=name, email=email, phone=phone,  address=address)
        user.save()
        self.stdout.write(f'{user}')