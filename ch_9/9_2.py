class Restaurant:
    def __init__(self, name, ctype):
        self.restaurant_name = name
        self.cuisine_type = ctype

    def describe_restaurant(self):
        print(f"Name: {self.restaurant_name.title()}\nCuisine: {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open for business!")

res_1 = Restaurant("El Cangrejo", "mariscos")
res_2 = Restaurant("Yard House", "various")
res_3 = Restaurant("Ono's", "Hawaiian BBQ")

res_1.describe_restaurant()
res_2.describe_restaurant()
res_3.describe_restaurant()
