from app.postcode import Postcode

user_input = input("Enter Postcode: \n")
postcode = Postcode(user_input)

keys = postcode.get_list_of_keys()
for key in keys:
    print(key)