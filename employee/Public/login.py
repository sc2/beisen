from api import ApiDemo


class Login:
    # 登录测试环境
    def login(self, url=None, data=None, header=None):
        self.ad = ApiDemo()
        login = ApiDemo.do_post(url, data, header)
        return login

    def Get_token(self, url=None, data=None, header=None):

        return ApiDemo.do_post((url, data, header))


