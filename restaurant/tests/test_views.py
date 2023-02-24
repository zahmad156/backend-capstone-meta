from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from ..models import Menu
from ..serializers import MenuSerializer


class MenuViewTest(APITestCase):
    def setUp(self):
        self.menu_item_1 = Menu.objects.create(Title='Chicken Burger', Price=8.99, Inventory=10)
        self.menu_item_2 = Menu.objects.create(Title='Cheese Pizza', Price=12.99, Inventory=5)
        self.serializer = MenuSerializer([self.menu_item_1, self.menu_item_2], many=True)

    def test_getall(self):
        url = reverse('menu_items')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.serializer.data)