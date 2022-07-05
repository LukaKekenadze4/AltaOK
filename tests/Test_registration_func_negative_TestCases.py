# Basic Imports
import allure
from pytest import assume
from driver import Driver
import time

# Pages Imports
from pages.MainPage import MainPage
from pages.RegistrationPage import RegistrPage
from pages.LoginPageModal import LoginPage
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

MP = MainPage()
RP = RegistrPage()
LP = LoginPage()


@allure.feature("Registration functionality")
@allure.story("###")
class Test_registration_functionality:
    @allure.title("click registration button")
    @allure.description("go to the main page and test if the registration button is working ")
    def test_click_registration_button(self):
        time.sleep(1)
        regist_button = MP.click_registration_login_button()
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

    # All Fields Are Empty
    @allure.title("click registration button")
    @allure.description("when I go to the register page i should confirm")
    def test_click_reg_button(self):
        reg_button = RP.click_registration()
        with assume:
            assert reg_button.text == 'რეგისტრაცია'
        reg_button.click()

    @allure.title("###")
    @allure.description("###")
    def test_check_valid_messages(self):
        email_valid = RP.check_mail_valid_mess()
        passwd_valid = RP.check_passwd_valid_mess()
        re_pass_valid = RP.check_re_pass_valid_mess()
        terms_valid = RP.check_terms_valid_mess()

        with assume:
            assert email_valid.text == "ელ-ფოსტა ელ-ფოსტა ველში არასწორია."
            assert passwd_valid.text == "ველი პაროლი აუცილებელია"
            assert re_pass_valid.text == "ველი დაადასტურეთ პაროლი აუცილებელია"
            assert terms_valid.text == "ველი დაეთანხმეთ საიტის მოხმარების წესებსა და პირობებს აუცილებელია"

        print("valid messages is correct")


