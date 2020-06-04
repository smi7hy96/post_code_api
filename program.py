from app.postcode import Postcode

postcode = Postcode('BS9 4BZ')

keys = postcode.get_list_of_keys()
for key in keys:
    print(key)