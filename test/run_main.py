import pytest
import os
# from  base.logger import Logger
#
# logger=Logger('root').getlog()

if __name__=='__main__':
    pytest.main(['-s','--alluredir','./report/xml'])
    os.system("allure generate report/xml/ -o report/html --clean")

    # logger.info("test end! Generate test report")