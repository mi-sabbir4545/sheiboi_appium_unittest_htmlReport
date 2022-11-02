import time

from Pages.languageopage import LanguagePage
from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage


class EnglishLanguageTest(BasePage):
    def test_english_language(self):
        lp = LanguagePage(self.driver)
        time.sleep(2)

        lp.click_EnglishLanguage()
        time.sleep(2)
        lp.click_nextbutton()

        ll = LoginPage(self.driver)
        ll.ClickLoginButton()
        time.sleep(2)
        ll.EmailAddress()
        time.sleep(2)
        ll.Password()

