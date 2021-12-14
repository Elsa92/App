# encoding: utf-8
import allure
import pytest
from appium.webdriver.common.mobileby import MobileBy
from faker import Faker

from PageObject.MessagePage.messagepage import MessagePage

@allure.feature('添加联系人')
class TestAddMember:


    def setup_class(self):
        self.faker = Faker('zh_CN')
        self.main = MessagePage()


    def teardown(self,num=5):
        for i in range(num):
            try:
                self.main.find_ele(MobileBy.XPATH, '//*[@text = "我的客户"]')
            except:
                self.main.mobile_back()

        self.main.find_and_click(MobileBy.XPATH, '//*[@text = "消息"]')


    def teardown_class(self):
        self.main.close()

    @allure.story('添加联系人成功')
    @allure.title('成功添加联系人')
    @pytest.mark.parametrize('name, phone', [('张三','15002833033')], ids=['添加联系人'])
    def test_add_contact_successful(self, name, phone):
        # name = self.faker.name()
        # phone = self.faker.phone_number()
        with allure.step('进入手动添加联系人界面'):
            addpage = self.main.goto_contantPage().goto_addmemberpage().goto_editmemberpage()
        with allure.step('输入联系人信息， 点击保存按钮。并且获取Toast消息'):
            result = addpage.input_info(name, phone).get_result()
        with allure.step('判断Toast消息是否正确'):
            assert result == '添加成功'

        with allure.step('保存图片'):
            allure.attach(self.main.get_screen(), '添加单个联系人', allure.attachment_type.PNG)

    @allure.story('添加联系人成功')
    @allure.title('成功连续添加联系人')
    def test_add_contacts_successful(self):
        name1 = self.faker.name()
        phone1 = self.faker.phone_number()
        name2 = self.faker.name()
        phone2 = self.faker.phone_number()
        with allure.step('进入手动添加联系人界面'):
            addpage = self.main.goto_contantPage().goto_addmemberpage().goto_editmemberpage()
        with allure.step('通过点击保存并连续添加， 添加两个联系人'):
            r = addpage.input_infos(name1, phone1, name2, phone2)

        with allure.step('点击返回按钮，回到通讯录界面,并获取姓名列表'):
            name_list = r.back_to_contactpage().get_namelist()
            assert name1, name2 in name_list

        with allure.step('保存图片'):
            allure.attach(self.main.get_screen(), '添加两个联系人成功', allure.attachment_type.PNG)



