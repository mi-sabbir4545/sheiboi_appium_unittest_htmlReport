from Pages.HomePage import HomePage
from Locators.locators import Login


class LoginPage(HomePage):

    def __init__(self, driver):
        self.locator = Login
        self.driver = driver
        super(LoginPage, self).__init__(driver)

    def ClickLoginButton(self):
        self.find_element(*self.locator.clickloginbutton_ID).click()

    def EmailAddress(self):
        self.find_element(*self.locator.emailaddress_ID).send_keys("sabbir722722@gmail.com")

    def Password(self):
        self.find_element(*self.locator.password_ID).send_keys("sabbir@123.com")
