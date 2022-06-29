# 测试环境登录
import json


import requests
import unittest
import sys
sys.path.append('../Public')
from Public.api import ApiDemo
from ddt import ddt, file_data


@ddt
class Mytest(unittest.TestCase):

    def setUp(self) -> None:
        self.url = "http://openapi.italent.link/Account/Account/LogInITalent"
        self.url_token = "http://openapi.italent.link/token"

        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        self.data1 = {
            'grant_type': 'client_credentials',
            'app_key': 'JFFxJwwTQMBtKivEJTM7VNZfwXVXFQ87',
            'app_secret': 'gaaxb4hBSwiToXc6Do9cs3Avw3QYuu4lDGB6u5tQOsLrbz2E9TWCgNPdPf2Zc0GX'
        }

    @file_data('./Data/user.yaml')
    def test_post(self, data):
        print(data)
        res = requests.post(url=self.url, data=data)
        res1 = requests.post(url=self.url_token, data=self.data1, headers=self.headers)

        print(res)
        print(res1)
        print(res1.text)

    def test_get(self):
        print("3")


if __name__ == '__main__':
    unittest.main()
