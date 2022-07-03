from pages.BasePage import BasePage
from locators.locators import Locators
import time


class MainPage(BasePage):
    def __init__(self):
        pass

    def click_registration_button(self):
        reg_button = BasePage.find_element(self, Locators.reg_button_xpath)
        return reg_button

    def click_registration_title(self):
        reg_title = BasePage.find_element(self, Locators.reg_title_xpath)
        return reg_title
