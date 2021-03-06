# Basic Imports
import allure
from pytest import assume
from driver import Driver
import time

# Pages Imports
from pages.MainPage import MainPage
from pages.RegistrationPage import Registr_Page
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
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# tests
MP = MainPage()
RP = Registr_Page()
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
            assert reg_title.text == '?????????????????????????????????'
        reg_title.click()

    # Registration Page Tests
    # """
    #     Positive Test Cases
    # """

    @allure.title("input mail")
    @allure.description("when I go to the register page i should input my own mail")
    def test_input_email(self):
        input_mail = RP.input_email()
        email_field_label = RP.email_field_label()
        with assume:
            assert email_field_label.text == '??????-???????????????'
        input_mail.send_keys('keke20@gmail.com')

    @allure.title("input registration password")
    @allure.description("when I go to the register page i should input my own password")
    def test_input_password(self):
        input_passwd = RP.input_passwd()
        passwd_field_label = RP.passwd_field_label()
        with assume:
            assert passwd_field_label.text == '??????????????????'
        input_passwd.send_keys('Kekenadze2020')

    @allure.title("input registration re-password")
    @allure.description("when I go to the register page i should input my own re-password")
    def test_input_re_password(self):
        input_re_passwd = RP.input_re_passwd()
        re_passwd_field_label = RP.re_passwd_field_label()
        with assume:
            assert re_passwd_field_label.text == '????????????????????????????????? ??????????????????'
        input_re_passwd.send_keys('Kekenadze2020')

    @allure.title("input name")
    @allure.description("when I go to the register page i should input my own name")
    def test_input_name(self):
        input_name = RP.input_name()
        name_field_label = RP.name_field_label()
        with assume:
            assert name_field_label.text == '??????????????????'
        input_name.send_keys('????????????')

    time.sleep(2)

    @allure.title("input surname")
    @allure.description("when I go to the register page i should input my own surname")
    def test_input_surname(self):
        input_surname = RP.input_surname()
        surname_field_label = RP.surname_field_label()
        with assume:
            assert surname_field_label.text == '???????????????'
        input_surname.send_keys('???????????????????????????')

    @allure.title("mark checkbox")
    @allure.description("when I go to the register page i should mark checkbox")
    def test_check_box(self):
        check = RP.check_box()
        check_box_title = RP.check_box_title()
        with assume:
            assert check_box_title.text == '?????????????????????????????? ?????????????????? ?????????????????????????????? ????????????????????? ?????? ????????????????????????'
        check.click()

    @allure.title("click registration button")
    @allure.description("when I go to the register page i should confirm")
    def test_click_reg_button(self):
        reg_button = RP.click_registration()
        with assume:
            assert reg_button.text == '?????????????????????????????????'
        reg_button.click()

    # LoginPageTests
    @allure.title("click login button")
    @allure.description("go to the main page and test if the login button is working")
    def test_click_login_button(self):
        login = MP.click_registration_login_button()
        login.click()
        time.sleep(2)

    @allure.title("input email")
    @allure.description("###")
    def test_input_email_login(self):
        input_email = LP.input_email_login()
        input_email.send_keys("keke20@gmail.com")

    @allure.title("input password")
    @allure.description("###")
    def test_input_passwd_login(self):
        input_passwd = LP.input_passwd_login()
        input_passwd.send_keys("Kekenadze2020")

    @allure.title("click login button in login modal")
    @allure.description("###")
    def test_click_submit_button(self):
        button_login = LP.click_submit_button()
        button_login.click()
