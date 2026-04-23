from django.test import TestCase, Client
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        Menu.objects.create(title="Pizza", price=12, inventory=50)
        Menu.objects.create(title="Pasta", price=9, inventory=30)
        Menu.objects.create(title="Salad", price=7, inventory=20)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), serializer.data)
