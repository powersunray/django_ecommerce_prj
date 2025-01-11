from django.contrib import admin
from .models import Product, Warehouse, Customer, Order, OrderItem, User

# Register your models here.
admin.site.register(Product)
admin.site.register(Warehouse)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(User)