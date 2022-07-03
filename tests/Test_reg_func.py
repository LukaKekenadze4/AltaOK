# Basic Imports
import allure
from pytest import assume
from driver import Driver
import time

#Pages Imports
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
        time.sleep(2)
        MP.click_registration_button()
        with assume:
            assert Driver.driver.title == "Alta.ge - Online Shopping For Electronics, Computers, " \
                                          "Notebooks, Smartphones, TV-s, Game Consoles, " \
                                          "Home Appliances and more"

    @allure.title("click registration title")
    @allure.description("when the modal window open,then click on the title of registration")
    def test_click_registration_title(self):
        reg_title = MP.click_registration_title()
        with assume:
            assert reg_title == 'რეგისტრაცია'

    @allure.title("input mail")
    @allure.description("when I go to the register page i should input my own mail")
    def test_input_email(self):
        RP.input_email()
