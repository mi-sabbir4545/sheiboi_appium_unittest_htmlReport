import time

from Pages.LoginPage import LoginPage
from Pages.BasePage import BasePage


class LoginPageTest(BasePage):

    def test_login_page(self):
        lp = LoginPage(self.driver)
        time.sleep(2)

        lp.ClickLoginButton()
        time.sleep(2)

