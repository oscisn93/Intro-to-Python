import unittest
from city_functions_ import city_country

class test_cities(unittest.TestCase):
    def test_city_country(self):
        city = 'los angeles'
        country = 'united states'
        result = city_country(city, country)
        self.assertEqual(result, 'Los Angeles, United States')

if __name__ == '__main__':
    unittest.main()
