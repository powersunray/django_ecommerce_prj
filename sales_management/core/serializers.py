from rest_framework import serializers # Import serializers from Django REST framework
from .models import Product, Warehouse, Customer, Order, OrderItem, User # Import models

class ProductSerializer(serializers.ModelSerializer):
    class Meta: # Meta class to define metadata
        model = Product # The model that this serializer will represent
        fields = '__all__' # Include all fields from the Product model

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
