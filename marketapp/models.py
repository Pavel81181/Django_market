
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    register_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, phone: {self.phone}, register_date: {self.register_date}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.DecimalField(max_digits=8, decimal_places=2)
    add_date = models.DateField(auto_now_add=True)
    image_product = models.ImageField(upload_to="images/")

    def __str__(self):
        return f'Productname: {self.name}, description: {self.description}, price: {self.price}, add_date: {self.add_date}'


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'customer: {self.customer.name}, products: {self.products.all()}, total_price: {self.total_price}, date: {self.date_ordered}'

