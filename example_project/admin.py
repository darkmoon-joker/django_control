from django.contrib import admin

from example_project import models


admin.site.register(models.Pizza)
admin.site.register(models.Restaurant)
admin.site.register(models.Order)
