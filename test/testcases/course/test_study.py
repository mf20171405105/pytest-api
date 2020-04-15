import allure
from conftest import http
from  common.commonDate import CommonDate

@allure.feature("学习动态")
class TestStudy:

    @allure.story("学习动态获取成功")
    def test_study_success(self):
        path="/api/courses/v3/trends"
        response=http.get(path)
