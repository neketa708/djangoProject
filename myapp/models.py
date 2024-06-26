from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number_client = models.IntegerField()
    address = models.TextField()
    registration_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    summ = models.DecimalField(max_digits=8, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Order ID: {self.id}, Client: {self.client}, Total Sum: {self.summ}"