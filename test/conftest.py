import pytest
from common.commonDate import CommonDate
from util.httpUtil import HttpUtil
from util.logger import Logger

http=HttpUtil()
logger=Logger(logname="session_fixture").getlog()
@pytest.fixture(scope='session',autouse=True)
def session_fixture():
    path="/api/auth/login"
    date = {'loginId': CommonDate.name,
            'password': CommonDate.password,
            'orgId': CommonDate.orgId}
    response=http.post(path,date)
    # CommonDate.token=response['object']['token']
    try:
        assert response['ok']==True
        logger.info("Login successfully")
        print("登录成功")
    except:
        print("登录失败"+response['ok'])
        logger.info("Login failure")




