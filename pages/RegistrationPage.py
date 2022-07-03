from pages.BasePage import BasePage
from locators.locators import Locators
import time


class RegistrPage(BasePage):
    def __init__(self):
        pass

    def input_email(self):
        input_mail = BasePage.find_element(self, Locators.email_field_ID)
        input_mail.send_keys('iniestaluka@gmail.com')