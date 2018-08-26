from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text="something really helpful")
    menu = models.ManyToManyField(Pizza, related_name='restaurants')

    def __str__(self):
        return self.name


class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='orders')
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name='orders')
