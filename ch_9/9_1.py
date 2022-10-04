class Restaurant:
    def __init__(self, name, ctype):
        self.restaurant_name = name
        self.cuisine_type = ctype

    def describe_restaurant(self):
        print(f"Name: {self.restaurant_name.title()}\nCuisine: {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open for business!")

res = Restaurant("El Cangrejo", "mariscos")
print(res.restaurant_name)
print(res.cuisine_type)
res.describe_restaurant()
res.open_restaurant()