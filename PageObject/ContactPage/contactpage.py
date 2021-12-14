from appium.webdriver.common.mobileby import MobileBy

from Common.basepage import BasePage
from PageObject.ContactPage.addmemberpage import AddMemberPage
from PageObject.ContactPage.manageaddresspage import ManageAddressPage


class ContactPage(BasePage):
    _add_member = (MobileBy.XPATH, '//*[@text="添加成员"]')
    _list = (MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/bn_"]//android.widget.TextView')
    _edit_icon = (MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/ixb"]')

    def goto_addmemberpage(self):
        # 点击添加成员，进入添加成员界面
        self.swipe_and_find(*self._add_member).click()
        return AddMemberPage(self.driver)

    def get_namelist(self):
        """
        获取成员列表
        :return:
        """
        lists = []
        eles = self.find_eles(*self._list)
        for value in eles:
            lists.append(value.text)
        return lists

    def goto_manageaddresspage(self):
        # 点击编辑按钮，进入管理通讯录界面
        self.find_and_click(*self._edit_icon)
        return ManageAddressPage(self.driver)
