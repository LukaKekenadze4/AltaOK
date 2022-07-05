from pages.BasePage import BasePage as BP
from locators.LoginPageLocators import LoginLocator

LPL = LoginLocator()


class LoginPage(BP):
    def __init__(self):
        pass

    def input_email_login(self):
        email_field = BP.find_element(self, LPL.Login_field_ID)
        return email_field

    def input_passwd_login(self):
        passwd_field = BP.find_element(self, LPL.paswd_field_ID)
        return passwd_field

    def click_submit_button(self):
        log_button = BP.find_element(self, LPL.login_button_modal)
        return log_button
