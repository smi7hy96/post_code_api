# POSTCODE API

This api allows the user to enter a postcode and a new object of Class Postcode will be created.

When any of the class methods are used, it will check for  a response from api.postcodes.io AND if successful produce information about the postcode.

The current functions available to the user are:

- get_list_of_keys() - This allows the user to see what information they could get, in case they have never used this before.

- get_certain_value(key_name) - Using one of those key names they can get the associated value of said key

- long_lat - returns the longitude and latitude of a postcode