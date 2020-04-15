import requests
import json
from common.commonDate import CommonDate
from  util.logger import Logger

logger=Logger(logname="HttpUtil").getlog()
class HttpUtil:
    def __init__(self):
        self.http=requests.session()
        self.header={"Content-Type":"application/json;charset=UTF-8"}


    def post(self,path,date):

        url=CommonDate.host+path
        # date_json=json.dumps(date) #json.dumps()用于将字典形式的数据转化为字符串，但在此处用就显示用户登录失败
        response=self.http.post(url,data=date)
        assert response.status_code==200
        resp_json=response.text
        response_dict=json.loads(resp_json) #json.loads()用于将字符串形式的数据转化为字典
        try:
            assert response_dict['ok']==True
            logger.info("Post responses successfully")
        except:
            logger.info("Post responses failure")
        return response_dict

    def get(self,path):
        response=self.http.get(url=CommonDate.host+path)
        assert response.status_code==200
        try:
            assert response.json()['ok']==True
            logger.info("Get responses successfully")
        except:
            logger.info("Get responses failure")
        return response


