name =  input("Hello, what is your name? ")
country_one = input("In what country would your dream vacationd be? ") 
country_two = input("What other country do you dream of vacationing in? ")
user = {
    "name": name,
    "destinations": [country_one, country_two]
}

print(f"User {user['name']} dreams of vacationing in {user['destinations'][0]} or {user['destinations'][1]}.")