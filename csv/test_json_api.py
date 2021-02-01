import unittest
from json_api import JsonApi

class TestJsonApi(unittest.TestCase):

    def test_get_key_value(self):
        url = "https://api.sncf.com/v1/coverage/sncf/stop_areas"
        auth=('b8d19b5e-f838-462b-9f30-334d98cd15a8','')
        json_stop_areas = JsonApi(url,auth)
        json_stop_areas.read_json_url()
        areas = json_stop_areas.json_data
        list_href = json_stop_areas.get_key_value(areas["links"],"href")
        self.assertIsNotNone(list_href)

if __name__ == '__main__':
    unittest.main()