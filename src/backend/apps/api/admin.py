from django.contrib import admin

from .models import Customer, Car, Comment


admin.site.register(Customer)
admin.site.register(Car)
admin.site.register(Comment)
