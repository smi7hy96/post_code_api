import unittest
from app.postcode import *

class PostcodeTest(unittest.TestCase):
    def setUp(self):
        self.postcode = Postcode('BN246AY')

    def test_get_list_of_keys(self):
        self.assertEqual(self.postcode.get_list_of_keys(), ['postcode', 'quality', 'eastings', 'northings', 'country', 'nhs_ha', 'longitude', 'latitude', 'european_electoral_region', 'primary_care_trust', 'region', 'lsoa',  'msoa',  'incode',  'outcode',  'parliamentary_constituency', 'admin_district', 'parish', 'admin_county', 'admin_ward', 'ced',  'ccg',  'nuts', 'codes'])

    def test_long_lat(self):
        self.assertEqual(self.postcode.long_lat(), 'Your Longitude is 0.349465, your latitude is 50.812043, your parliamentary constituency is Bexhill and Battle and your NUTS value is: East Sussex CC')

    def test_get_certain_value(self):
        self.assertEqual(self.postcode.get_certain_value('country'), 'England')
        self.postcode.postcode = 'BNNNNNN'
        self.assertEqual(self.postcode.get_certain_value('country'), 'Error occurred when retrieving postcode (error message 404)')
