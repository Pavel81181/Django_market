from django.core.management.base import BaseCommand
from marketapp.models import User, Product, Order

class Command(BaseCommand):
    help = "Create order."

    def add_arguments(self, parser):
        parser.add_argument("user_id", type=int, help="user ID")
        parser.add_argument('-p', '--id_product', nargs='*', help="product ID", required=True)


    def handle(self, *args, **kwargs):
        user_id = kwargs.get('user_id')
        id_product: list = kwargs.get('id_product')  # запись в id_product  параметров из командной строки

        user = User.objects.filter(pk=user_id).first()

        order = Order(customer=user)
        total_price = 0
        for i in range(0, len(id_product)):
            product = Product.objects.filter(pk=id_product[i]).first()
            total_price += float(product.price)
            order.total_price = total_price
            order.save()
            order.products.add(product)
        self.stdout.write(f'{order}')