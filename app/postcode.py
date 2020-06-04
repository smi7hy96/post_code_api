import requests


class Postcode:
    def __init__(self, postcode):
        self.postcode = postcode

    def __get_response(self):
        response = requests.get('http://api.postcodes.io/postcodes/' + self.postcode)
        return response

    def get_list_of_keys(self):
        response = self.__get_response()
        if self.__error_handle(response):
            return self.__all_keys(response)
        else:
            return f'Error occurred when retrieving postcode (error message {response.status_code})'

    def __all_keys(self, response):
        response_dict = response.json()['result']
        keys_list = []
        for keys in response_dict:
            keys_list.append(keys)
        return keys_list

    def long_lat(self):
        response = self.__get_response()
        if self.__error_handle(response):
            response_dict = response.json()['result']
            long = response_dict['longitude']
            lat = response_dict['latitude']
            pm_con = response_dict['parliamentary_constituency']
            nuts = response_dict['nuts']

            return f'Your Longitude is {long}, your latitude is {lat}, your parliamentary constituency is {pm_con} and your NUTS value is: {nuts}'
        else:
            return self.__error_handle(response)

    def get_certain_value(self, key_name):
        response = self.__get_response()
        if self.__error_handle(response):
            return response.json()['result'][key_name]
        else:
            return f'Error occurred when retrieving postcode (error message {response.status_code})'

    def __error_handle(self, response):
        if str(response.status_code).startswith('2') or str(response.status_code).startswith('3'):
            return True
        else:
            return False