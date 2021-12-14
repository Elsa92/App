from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from Common.basepage import BasePage



class EditMemberPage(BasePage):
    _name = (MobileBy.XPATH, '//*[@text="姓名　"]/..//android.widget.EditText')
    _phone = (MobileBy.XPATH, '//*[@text="手机　"]/..//android.widget.EditText')
    _check_box = (MobileBy.XPATH, '//*[@text= "保存后自动发送邀请通知"]')
    _save_button = (MobileBy.XPATH, '//*[@text= "保存"]')
    _text = (MobileBy.XPATH, '//*[@resource-id="android:id/content"]/android.widget.LinearLayout/android.widget.RelativeLayout[1]')
    _save_and_edit = (MobileBy.XPATH, '//*[@text = "保存并继续添加"]')

    def input_info(self, name, phone):
        # 输入姓名， 电话号码， 点击保存按钮
        from PageObject.ContactPage.addmemberpage import AddMemberPage
        self.find_and_sendkeys(*self._name, name)
        self.find_and_sendkeys(*self._phone, phone)
        self.find_and_click(*self._check_box)
        self.find_and_click(*self._save_button)

        return AddMemberPage(self.driver)

    def input_infos(self, name1, phone1, name2, phone2):
        """
        输入联系人1的姓名、电话 点击保存并继续添加
        输入联系人2的姓名、电话 点击保存按钮
        :param name1:
        :param phone1:
        :param name2:
        :param phone2:
        :return:
        """
        from PageObject.ContactPage.addmemberpage import AddMemberPage
        self.find_and_sendkeys(*self._name, name1)
        self.find_and_sendkeys(*self._phone, phone1)
        self.find_and_click(*self._check_box)
        self.find_and_click(*self._save_and_edit)
        sleep(5)
        self.find_and_sendkeys(*self._name, name2)
        self.find_and_sendkeys(*self._phone, phone2)
        self.find_and_click(*self._save_button)
        return AddMemberPage(self.driver)
