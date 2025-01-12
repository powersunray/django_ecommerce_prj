from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Product, Warehouse, Customer, Order, OrderItem, User

# Create your tests here.
class ProductTests(APITestCase):
    def setUp(self):
        self.warehouse = Warehouse.objects.create(name='Warehouse 1', location='Test Location')
    def test_create_product(self):
        url = reverse('product-list')
        data = {
            'name': 'Test Product',
            'description': 'Test Description',
            'price': 100.00,
            'quantity': 10,
            # 'warehouse': 1
            'warehouse': self.warehouse.id # Ensure the warehouse is referenced by its ID
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class WarehouseTests(APITestCase):
    def test_create_warehouse(self):
        url = reverse('warehouse-list')
        data = {'name': 'Test Warehouse', 'location': 'Test Location'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class CustomerTests(APITestCase):
    def test_create_customer(self):
        url = reverse('customer-list')
        data = {
            'name': 'Test Customer',
            'email': 'test@example.com',
            'phone': '0123456789',
            'address': 'Test Address'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class OrderTests(APITestCase):
    def setUp(self):
        self.customer = Customer.objects.create(name='Test Customer', email='test@example.com', phone='0123456789', address='Test Address')

    def test_create_order(self):
        url = reverse('order-list')
        data = {
            'customer': self.customer.id,
            'status': 'pending'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class OrderItemTests(APITestCase):
    def setUp(self):
        self.customer = Customer.objects.create(name='Test Customer', email='test@example.com', phone='0123456789', address='Test Address')
        self.order = Order.objects.create(customer=self.customer, status='pending')
        self.warehouse = Warehouse.objects.create(name='Warehouse 1', location='Test Location')
        self.product = Product.objects.create(name='Test Product', description='Test Description', price=100, warehouse=self.warehouse)

    def test_create_order_item(self):
        url = reverse('orderitem-list')
        data = {
            'order': self.order.id,
            'product': self.product.id,
            'quantity': 2
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class UserTests(APITestCase):
    def test_create_user(self):
        url = reverse('user-list')
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password123',
            'role': 'admin'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
# Run them: python manage.py test