from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException


class BasePage:

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            caps = {
                'platformName': 'Android',
                'deviceName': '127.0.0.1:7555',
                'appPackage': 'com.tencent.wework',
                'appActivity': '.launch.WwMainActivity',
                'noReset': 'True',
                'unicodeKeyBoard': 'True',
                'resetKeyBoard': 'True'
            }

            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
            self.driver.implicitly_wait(10)
        else:
            self.driver = driver


    def find_ele(self, by, locator):
        ele = self.driver.find_element(by, locator)
        return ele

    def find_eles(self, by, locator):
        eles = self.driver.find_elements(by, locator)
        return eles

    def find_and_click(self, by, locator):
        ele = self.find_ele(by, locator)
        ele.click()

    def find_and_sendkeys(self, by, locator, text):
        self.driver.find_element(by, locator).send_keys(text)

    def swipe_and_find(self, by, locator, num=3):

        for i in range(num):
            try:
                ele = self.find_ele(by, locator)
                return ele
            except:
                window_size = self.driver.get_window_size()
                width = window_size['width']
                height = window_size['height']
                start_x = width/2
                start_y = height * 0.8
                end_x = start_x
                end_y = height * 0.2
                self.driver.swipe(start_x, start_y, end_x, end_y, duration=2000)

            if i == num-1:
                raise NoSuchElementException(f'找了{i+1}次，没有找到该元素')

    def close(self):
        self.driver.quit()

    def back(self):
        self.driver.back()

    def mobile_back(self):
        self.driver.keyevent(4)

    def get_toast_text(self):
        result = self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
        return result

    def get_screen(self):
        screenshot = self.driver.get_screenshot_as_png()
        return screenshot