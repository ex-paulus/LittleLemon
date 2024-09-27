from django.test import TestCase
from restaurant.views import Menu

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=2, inventory=10)
        item_string = item.get_item()
        self.assertEqual(item_string, "IceCream : 2")