# Basic Imports
import allure
from pytest import assume
from driver import Driver
import time

# Pages Imports
from pages.MainPage import MainPage
from pages.RegistrationPage import RegistrPage
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# clear reports files(images/allure)
import os

mypath = "reports/images"
mypath1 = "reports/allure"
for root, dirs, files in os.walk(mypath):
    for file in files:
        os.remove(os.path.join(root, file))

for root, dirs, files in os.walk(mypath1):
    for file in files:
        os.remove(os.path.join(root, file))
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# tests
MP = MainPage()
RP = RegistrPage()


@allure.feature("Registration functionality")
@allure.story("###")
class Test_registration_functionality:
    @allure.title("click registration button")
    @allure.description("go to the main page and test if the registration button is working ")
    def test_click_registration_button(self):
        time.sleep(1)
        regist_button = MP.click_registration_button()
        with assume:
            assert Driver.driver.title == "Alta.ge - Online Shopping For Electronics, Computers, " \
                                          "Notebooks, Smartphones, TV-s, Game Consoles, " \
                                          "Home Appliances and more"
        regist_button.click()

    @allure.title("click registration title")
    @allure.description("when the modal window open,then click on the title of registration")
    def test_click_registration_title(self):
        reg_title = MP.click_registration_title()
        with assume:
            assert reg_title.text == 'რეგისტრაცია'
        reg_title.click()

    # Registration Page Tests
    @allure.title("input mail")
    @allure.description("when I go to the register page i should input my own mail")
    def test_input_email(self):
        input_mail = RP.input_email()
        email_field_label = RP.email_field_label()
        with assume:
            assert email_field_label.text == 'ელ-ფოსტა'
        input_mail.send_keys('luka1@gmail.com')

    @allure.title("input password")
    @allure.description("when I go to the register page i should input my own password")
    def test_input_password(self):
        input_passwd = RP.input_passwd()
        passwd_field_label = RP.passwd_field_label()
        with assume:
            assert passwd_field_label.text == 'პაროლი'
        input_passwd.send_keys('Kekenadze2020')

    @allure.title("input re-password")
    @allure.description("when I go to the register page i should input my own re-password")
    def test_input_re_password(self):
        input_re_passwd = RP.input_re_passwd()
        re_passwd_field_label = RP.re_passwd_field_label()
        with assume:
            assert re_passwd_field_label.text == 'დაადასტურეთ პაროლი'
        input_re_passwd.send_keys('Kekenadze2020')

    @allure.title("input name")
    @allure.description("when I go to the register page i should input my own name")
    def test_input_name(self):
        input_name = RP.input_name()
        name_field_label = RP.name_field_label()
        with assume:
            assert name_field_label.text == 'სახელი'
        input_name.send_keys('ზაურ')

    time.sleep(2)

    @allure.title("input surname")
    @allure.description("when I go to the register page i should input my own surname")
    def test_input_surname(self):
        input_surname = RP.input_surname()
        surname_field_label = RP.surname_field_label()
        with assume:
            assert surname_field_label.text == 'გვარი'
        input_surname.send_keys('კორინთელი')

    @allure.title("mark checkbox")
    @allure.description("when I go to the register page i should mark checkbox")
    def test_check_box(self):
        check = RP.check_box()
        check_box_title = RP.check_box_title()
        with assume:
            assert check_box_title.text == 'დაეთანხმეთ საიტის მოხმარების წესებსა და პირობებს'
        check.click()

    @allure.title("click registration button")
    @allure.description("when I go to the register page i should confirm")
    def test_click_reg_button(self):
        reg_button = RP.click_registration()
        # with assume:
        #     assert reg_button.text == 'რეგისტრაცია'
        reg_button.click()
