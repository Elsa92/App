import os

import pytest

if __name__ == '__main__':
    pytest.main(['./test_add_member.py','--alluredir','./allure-results'])
    os.system('allure serve ./allure-results -o ./report --clean')