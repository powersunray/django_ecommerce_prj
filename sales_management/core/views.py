from django.shortcuts import render
from rest_framework import viewsets # Import viewsets from Django REST framework
from .models import Product, Warehouse, Customer, Order, OrderItem, User # Import models
from .serializers import ProductSerializer, WarehouseSerializer, CustomerSerializer, OrderSerializer, OrderItemSerializer, UserSerializer # Import serializers

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet): # Create a viewset for the Product model
    queryset = Product.objects.all() # Define the queryset
    serializer_class = ProductSerializer # Define the serializer class

class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer