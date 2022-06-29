# 环境登录
import requests
import unittest
from ddt import ddt, file_data


@ddt
class Mytest(unittest.TestCase):

    def setUp(self):
        pass

    @file_data('./Data/url.yaml')
    def test_01(self, data):


        res_login = requests.post(url=data['url_login'], data=data['data_login'])
        res_token = requests.post(url=data['url_token'], data=data['data_token'], headers=data["headers_token"])

        txt = "bearer"
        self.assertEqual(txt, res_token.json()["token_type"], '断言失败')

    def test_02(self):
        print("3")

    def test_03(self):
        print("4")


if __name__ == '__main__':
    unittest.main()
