from pages.BasePage import BasePage
from locators.MainPageLocators import MainLocators

MPL = MainLocators()


class MainPage(BasePage):
    def __init__(self):
        pass

    def click_registration_login_button(self):
        reg_button = BasePage.find_element(self, MPL.reg_button_xpath)
        return reg_button

    def click_registration_title(self):
        reg_title = BasePage.find_element(self, MPL.reg_title_xpath)
        return reg_title
