import allure
from appium.webdriver.common.mobileby import MobileBy
from faker import Faker

from PageObject.MessagePage.messagepage import MessagePage

@allure.feature('添加部门')
class TestAddDepartment:

    def setup_class(self):
        self.faker = Faker('zh_CN')
        self.main = MessagePage()

    def teardown(self, num=5):
        for i in range(num):
            try:
                self.main.find_ele(MobileBy.XPATH, '//*[@text = "我的客户"]')
            except:
                self.main.mobile_back()

        self.main.find_and_click(MobileBy.XPATH, '//*[@text = "消息"]')

    def teardown_class(self):
        self.main.close()

    @allure.story('添加子部门')
    @allure.title('成功添加子部门')
    def test_add_department_successful(self,depart_name):
        with allure.step('进入添加子部门界面'):
            addpage = self.main.goto_contantPage().goto_manageaddresspage().goto_adddepartment()
        with allure.step('输入部门名称，点击保存按钮.并获取部门列表'):
            depart_list = addpage.edit_department_info(depart_name).get_department_list()
        with allure.step('判断新添加的部门有没有列表里'):
            assert depart_name in depart_list
        with allure.step('保存截图'):
            allure.attach(self.main.get_screen(), '添加成功', allure.attachment_type.PNG)
