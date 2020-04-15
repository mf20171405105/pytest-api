from common.commonDate import CommonDate
from conftest import http
import allure

@allure.feature("登录模块")
class Test_login:

    @allure.story("登陆成功")
    def test_success(self):
        path = "/api/auth/login"
        date = {"loginId": CommonDate.name, "password": CommonDate.password, "orgId": CommonDate.orgId}
        response = http.post(path, date)

    def test_fail(self):
        path = "/api/auth/login"
        date = {"loginId": CommonDate.name, "password": "111111", "orgId": CommonDate.orgId}
        response = http.post(path, date)



