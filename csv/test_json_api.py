import unittest
from json_api import JsonSncfApi

class TestJsonApi(unittest.TestCase):

    def test_get_key_value(self):
        url = "https://api.sncf.com/v1/coverage/sncf/stop_areas"
        json_stop_areas = JsonSncfApi()
        json_stop_areas.set_url(url)
        json_stop_areas.read_json_url()
        areas = json_stop_areas.json_data
        json_stop_areas.get_key_values("href",areas)
        list_hrefs = json_stop_areas.list_hrefs
        self.assertIsNotNone(list_hrefs)

if __name__ == '__main__':
    unittest.main()