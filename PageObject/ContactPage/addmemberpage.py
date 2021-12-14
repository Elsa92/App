from appium.webdriver.common.mobileby import MobileBy

from Common.basepage import BasePage
from PageObject.ContactPage.editmemberpage import EditMemberPage
# from PageObject.ContactPage.contactpage import ContactPage


class AddMemberPage(BasePage):
     _manually_add = (MobileBy.XPATH, '//*[@text="手动输入添加"]')
     _back_button = (MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/iwk"]')

     def goto_editmemberpage(self):
          # 点击手动添加选项， 进入输入成员信息界面
          self.find_and_click(*self._manually_add)
          return EditMemberPage(self.driver)

     def get_result(self):
          # 获取Toast 的消息
          result = self.get_toast_text()
          return result

     def back_to_contactpage(self):
          # 点击back按钮， 回到通讯录界面
          self.find_and_click(*self._back_button)
          from PageObject.ContactPage.contactpage import ContactPage
          return ContactPage(self.driver)


