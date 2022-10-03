def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',location='princeton',field='physics', hobby='violin')
print(user_profile)

if 'hobby' in user_profile:
    print("Hobby is present")
    
my_profile = build_profile("oscar", "cisneros", major="computer science", strength="web development", weakness="multithreaded programming")
print(my_profile)