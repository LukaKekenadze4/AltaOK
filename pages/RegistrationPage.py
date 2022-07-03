from pages.BasePage import BasePage
from locators.locators import Locators
import time


class RegistrPage(BasePage):
    def __init__(self):
        pass

    def input_email(self):
        mail_field = BasePage.find_element(self, Locators.email_field_ID)
        return mail_field

    def email_field_label(self):
        email_label = BasePage.find_element(self, Locators.email_field_label_xpath)
        return email_label

    def input_passwd(self):
        passwd_field = BasePage.find_element(self, Locators.passwd_field_ID)
        return passwd_field

    def passwd_field_label(self):
        passwd_label = BasePage.find_element(self, Locators.passwd_field_label_xpath)
        return passwd_label

    def input_re_passwd(self):
        re_passwd_field = BasePage.find_element(self, Locators.re_passwd_field_ID)
        return re_passwd_field

    def re_passwd_field_label(self):
        re_passwd_label = BasePage.find_element(self, Locators.re_passwd_field_label_xpath)
        return re_passwd_label

    def input_name(self):
        name_field = BasePage.find_element(self, Locators.name_field_ID)
        return name_field

    def name_field_label(self):
        name_label = BasePage.find_element(self, Locators.name_field_label_xpath)
        return name_label

    def input_surname(self):
        surname_field = BasePage.find_element(self, Locators.surname_field_ID)
        return surname_field

    def surname_field_label(self):
        surname_label = BasePage.find_element(self, Locators.surname_field_label_xpath)
        return surname_label

    def check_box(self):
        check_box = BasePage.find_element(self, Locators.check_box_ID)
        return check_box

    def check_box_title(self):
        checkbox_label = BasePage.find_element(self, Locators.check_box_title_xpath)
        return checkbox_label

    def click_registr_button(self):
        registration_button = BasePage.find_element(self, Locators.registration_button_xpath)
        return registration_button
