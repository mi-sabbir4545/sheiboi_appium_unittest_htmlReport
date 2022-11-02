from Pages.HomePage import HomePage
from Locators.locators import EnglishLanguage


class LanguagePage(HomePage):

    def __init__(self, driver):
        self.locator = EnglishLanguage
        self.driver = driver
        super(LanguagePage, self).__init__(driver)

    def click_EnglishLanguage(self):
        self.find_element(*self.locator.engLanguage_ID).click()

    def click_nextbutton(self):
        self.find_element(*self.locator.nextbutton_ID).click()
