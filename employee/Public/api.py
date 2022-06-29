import requests


class ApiDemo:
    # post请求
    def do_post(self, url=None, params=None, headers=None, **kwargs):
        return requests.post(url=url, params=params, headers=headers, **kwargs)

    # get请求
    def do_get(self, url=None, params=None, headers=None, **kwargs):
        return requests.get(url=url, params=params, headers=headers, **kwargs)
