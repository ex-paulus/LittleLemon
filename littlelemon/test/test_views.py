from django.test import TestCase
from restaurant.views import Menu

""" class MenuViewTest(TestCase):   
    def setUp(self):
        self.item_one = Menu.objects.create(title="IceCream", price=2, inventory=10)
        self.item_two = Menu.objects.create(title="Orange Juice", price=1, inventory=11)
         
    def test_getall(self):
        items = Menu.objects.all()
        self.assertEqual(2, items.count) """