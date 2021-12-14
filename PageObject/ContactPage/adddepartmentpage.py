from appium.webdriver.common.mobileby import MobileBy

from Common.basepage import BasePage


class AddDepartmentPage(BasePage):
    _department_name = (MobileBy.XPATH, '//*[@text = "请输入部门名称"]')
    _confirm_button = (MobileBy.XPATH, '//*[@text = "确定"]')

    def edit_department_info(self,departmentname):
        self.find_and_sendkeys(*self._department_name, departmentname)
        self.find_and_click(*self._confirm_button)
        from PageObject.ContactPage.manageaddresspage import ManageAddressPage
        return ManageAddressPage(self.driver)


