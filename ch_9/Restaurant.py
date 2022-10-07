# 9_4

class Restaurant:
    def __init__(self, name, ctype):
        self.restaurant_name = name
        self.cuisine_type = ctype
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Name: {self.restaurant_name.title()}\nCuisine: {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open for business!")

    def set_number_served(self, num):
        self.number_served = num

    def increment_number_served(self, number):
        self.number_served += number

# restaurant = Restaurant("McDonalds", "Garbage")
# print('Number served:',restaurant.number_served)
# restaurant.number_served = 1000000000
# print('Number served:',restaurant.number_served)

# restaurant.set_number_served(40000000000)
# print('Number served:',restaurant.number_served)

# restaurant.increment_number_served(9800000)
# print('Number served:',restaurant.number_served)
