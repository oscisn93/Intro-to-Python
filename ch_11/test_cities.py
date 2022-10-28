import unittest
from city_functions import city_country

class test_cities(unittest.TestCase):
    def test_city_country(self):
        city = 'los angeles'
        country = 'united states'
        population = 4097000
        result = city_country(city, country, population)
        self.assertEqual(result, 'Los Angeles, United States - population 4097000.')

if __name__ == '__main__':
    unittest.main()