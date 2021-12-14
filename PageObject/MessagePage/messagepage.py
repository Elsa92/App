from appium.webdriver.common.mobileby import MobileBy

from Common.basepage import BasePage
from PageObject.ContactPage.contactpage import ContactPage


class MessagePage(BasePage):
    _contact_menu = (MobileBy.XPATH, '//*[@text="通讯录"]')

    def goto_contantPage(self):
        # 点击通讯录icon
        self.find_and_click(*self._contact_menu)
        return ContactPage(self.driver)
