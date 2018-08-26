# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from random import choices

from django.db import migrations


PIZZA_NAMES = [
    'Cheese',
    'Hawaiian',
    'Pepperoni',
    "Meat Lover's",
    'Sausage',
    'Supreme',
    "Veggie Lover's",
]

RESTAURANT_NAMES = [
    'Ciao',
    'Mama',
    'Pizza 𝜋',
    'Sicilia',
]


def get_model(apps, model_name):
    return apps.get_model('example_project', model_name)


def create_pizzas(apps, schema_editor):
    Pizza = get_model(apps, 'Pizza')
    Pizza.objects.bulk_create([Pizza(name=name) for name in PIZZA_NAMES])


def delete_pizzas(apps, schema_editor):
    Pizza = get_model(apps, 'Pizza')
    Pizza.objects.filter(name__in=PIZZA_NAMES).delete()


def create_restaurants(apps, schema_editor):
    Pizza = get_model(apps, 'Pizza')
    Restaurant = get_model(apps, 'Restaurant')

    all_pizzas = list(Pizza.objects.all())
    for name in RESTAURANT_NAMES:
        _create_restaurant(Restaurant, name, all_pizzas)

def _create_restaurant(Restaurant, name, menu):
    restaurant = Restaurant.objects.create(name=name)
    restaurant.menu.set(menu)
    restaurant.save()
    return restaurant


def delete_restaurants(apps, schema_editor):
    Restaurant = get_model(apps, 'Restaurant')
    Restaurant.objects.filter(name__in=RESTAURANT_NAMES).delete()


def create_orders(apps, schema_editor):
    Pizza = get_model(apps, 'Pizza')
    Restaurant = get_model(apps, 'Restaurant')
    Order = get_model(apps, 'Order')

    all_pizzas = list(Pizza.objects.all())
    all_restaurants = list(Restaurant.objects.all())
    order_count = 20
    Order.objects.bulk_create(
        Order(pizza=pizza, restaurant=restaurant)
        for pizza, restaurant in zip(choices(all_pizzas, k=order_count),
                                     choices(all_restaurants, k=order_count))
    )


class Migration(migrations.Migration):

    dependencies = [
        ('example_project', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_pizzas, reverse_code=delete_pizzas),
        migrations.RunPython(create_restaurants, reverse_code=delete_restaurants),
        # Cascading deletes will handle deletion of Orders
        migrations.RunPython(create_orders, reverse_code=migrations.RunPython.noop),
    ]
