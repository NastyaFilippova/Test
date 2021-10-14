import requests
import json
import unittest
import pytest
from pprint import pprint

token = 'AQAAAABZSJaaAADLW9_OGM1l8EInjyGO_csts40'
url = 'https://cloud-api.yandex.net/v1/disk/resources/'

headers = {"accept": "application/json",
"Authorization": token
}
params = {'path': 'Test',
          'overwrite': True}

r = requests.put(url=url, params=params, headers=headers)

class Test_check_requests:

    @classmethod
    def setup_class(cls):
        print("setup_class")

    def setup(self):
        print("setup")

    def test_status_code_200(self):
        res = requests.get(url=url, params=params, headers=headers)
        assert res.status_code == 200

    def test_status_code_404(self):
        res = requests.get(url=url, params=params, headers=headers)
        assert res.status_code != 404

    def test_dir_is_created(self):
        get_params = {'path': "/"}
        response = requests.get(url=url, params=get_params, headers=headers)
        res = response.json()
        for elements in res['_embedded']['items']:
            if params['path'] in elements['name']:
                assert True

    def tearDown(self):
        print("teardown")

    @classmethod
    def tearDown_class(cls):
        print("tearDown_class")

