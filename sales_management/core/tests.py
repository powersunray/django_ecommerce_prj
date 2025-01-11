from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Product, Warehouse, Customer, Order, OrderItem, User

# Create your tests here.
class ProductTests(APITestCase):
    def test_create_product(self):
        url = reverse('product-list')
        data = {'name': 'Test Product', 'description': 'Test Description', 'price': 100, 'quantity': 10, 'warehouse': 1}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class WarehouseTests(APITestCase):
    def test_create_warehouse(self):
        url = reverse('warehouse-list')
        data = {'name': 'Test Warehouse', 'address': 'Test Address'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class CustomerTests(APITestCase):
    def test_create_customer(self):
        url = reverse('customer-list')
        data = {'name': 'Test Customer', 'address': 'Test Address', 'phone': '0123456789'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

# Run them: python manage.py test