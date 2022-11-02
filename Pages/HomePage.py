from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
# from Locators import Locators


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        # self.base_url = base_url
        self.timeout = 30

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    # def go_back(self):
    #     self.driver.back()
    # base_url = ""