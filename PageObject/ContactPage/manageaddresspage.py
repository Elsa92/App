from appium.webdriver.common.mobileby import MobileBy

from Common.basepage import BasePage
from PageObject.ContactPage.adddepartmentpage import AddDepartmentPage


class ManageAddressPage(BasePage):
    _add_depart_button = (MobileBy.XPATH, '//*[@text = "添加子部门"]')
    _department_list = (MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/bn_"]//android.widget.TextView')

    def goto_adddepartment(self):
        self.find_and_click(*self._add_depart_button)
        return AddDepartmentPage(self.driver)

    def get_department_list(self):
        department_list = []
        eles = self.find_eles(*self._department_list)

        for value in eles:
            department_list.append(value.text)
        return department_list

