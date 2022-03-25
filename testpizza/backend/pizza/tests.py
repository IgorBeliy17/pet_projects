from django.test import TestCase, Client
from .models import Topping, Pizza


class PizzaTestCase(TestCase):

    def setUp(self):
        t1 = Topping.objects.create(name='курица', description='описание курицы')
        t2 = Topping.objects.create(name='петрушка', description='описание курицы')
        Pizza.objects.create(name='тестовая', toppings=[t1, t2], description='описание тестовой пиццы', slug='testpizza1')
    #
    # def test_valid_pizza(self):
    #     t1 = Topping.objects.create(name='курица', description='описание курицы')
    #     t2 = Topping.objects.create(name='петрушка', description='описание курицы')
    #     p = Pizza.objects.create(name='тестовая', toppings=[t1, t2], description='описание тестовой пиццы', slug='testpizza1')
    #     self.assertTrue(p.is_valid_pizza())
    #
    # def test_invalid_pizza(self):
    #     t1 = Topping.objects.get(name='курица')
    #     p = Pizza.objects.create(name='тестовая', toppings=0, description='описание тестовой пиццы', slug='testpizza1')
    #     self.assertFalse(p.is_valid_pizza())
    #
    # def test_pizzas_view(self):
    #     c = Client()
    #     response = c.get("/pizza/")
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.context["pizzas"].count(), 1)
    #
    # def test_pizza_api_get(self):
    #     c = Client()
    #     response = c.get("/api/v1/pizza/testpizza1/")
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.json()['name'], 'тестовая')
    #
    # def test_flight_api_post(self):
    #     c = Client()
    #     data = {
    #         "name": 'тестовая2',
    #         'toppings': [1, 2],
    #         "description": 'описание тестовой пиццы',
    #         'slug': 'testpizza2'
    #     }
    #     response = c.post("/api/v1/pizza/", data=data)
    #     self.assertEqual(response.status_code, 201)
    #     try:
    #         print(Pizza.objects.get(pk=2))
    #     except Pizza.DoesNotExist:
    #         print('Нет объекта с таким ключом')











