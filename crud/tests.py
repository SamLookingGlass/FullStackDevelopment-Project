from django.test import TestCase
from .models import Item

# Create your tests here.
class ItemTests(TestCase):
    
    def test_str(self):
        test_name = Item(name='A Product')
        self.assertEqual(str(test_name), 'A Product')