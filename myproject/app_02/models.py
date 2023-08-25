from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Name Customer: {self.name} Email: {self.email} Phone: {self.phone_number}"

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    addition_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Рroduct: {self.name} Price: {self.price} Quantity: {self.quantity}"

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    placement_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.customer} on {self.placement_date}"

