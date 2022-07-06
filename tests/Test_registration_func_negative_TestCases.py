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

MP = MainPage()
RP = Registr_Page()
LP = LoginPage()


@allure.feature("Registration functionality")
@allure.story("I test registration functionality with negative test cases")
class Test_registration_functionality:
    # TC01 All Fields Are Empty
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

    @allure.title("click submit button")
    @allure.description("when I go to the register page and input according datas then i should confirm it")
    def test_click_reg_button_2(self):
        reg_button = RP.click_registration()
        with assume:
            assert reg_button.text == 'რეგისტრაცია'
        reg_button.click()

    @allure.title("check validations N1")
    @allure.description("when i submit my own datas, the website should send error messages")
    def test_check_valid_messages_1(self):
        email_valid = RP.check_mail_valid_mess()
        passwd_valid = RP.check_passwd_valid_mess()
        re_pass_valid = RP.check_re_pass_valid_mess()
        terms_valid = RP.check_terms_valid_mess()

        with assume:
            assert email_valid.text == "ელ-ფოსტა ელ-ფოსტა ველში არასწორია."
            assert passwd_valid.text == "ველი პაროლი აუცილებელია"
            assert re_pass_valid.text == "ველი დაადასტურეთ პაროლი აუცილებელია"
            assert terms_valid.text == "ველი დაეთანხმეთ საიტის მოხმარების წესებსა და პირობებს აუცილებელია"

        print("\n valid messages is correct")

    # TC02 Only mail field is filled the rest is empty

    @allure.title("input registration mail")
    @allure.description("when I go to the register page i should input mail")
    def test_input_email(self):
        input_mail = RP.input_email()
        email_field_label = RP.email_field_label()
        with assume:
            assert email_field_label.text == 'ელ-ფოსტა'
        input_mail.send_keys('keke20@gmail.com')

    @allure.title("click submit button")
    @allure.description("when I go to the register page, i should confirm it")
    def test_click_reg_button_2(self):
        reg_button = RP.click_registration()
        with assume:
            assert reg_button.text == 'რეგისტრაცია'
        reg_button.click()

    @allure.title("check validations N2")
    @allure.description("when i submit my own datas, the website should send error messages")
    def test_check_valid_message_2(self):
        passwd_valid = RP.check_passwd_valid_mess()
        re_pass_valid = RP.check_re_pass_valid_mess()
        terms_valid = RP.check_terms_valid_mess()

        with assume: assert passwd_valid.text == "ველი პაროლი აუცილებელია"
        with assume: assert re_pass_valid.text == "ველი დაადასტურეთ პაროლი აუცილებელია"
        with assume: assert terms_valid.text == "ველი დაეთანხმეთ საიტის მოხმარების წესებსა და პირობებს აუცილებელია"

    @allure.title("clear email field")
    @allure.description("when the test have done, i should clear the field of email")
    def test_clear_email_field(self):
        input_mail = RP.input_email()
        input_mail.clear()

    # TC03 Only Password field is filled the rest is empty
    @allure.title("input registration password")
    @allure.description("when I go to the register page i should input password")
    def test_input_password(self):
        input_passwd = RP.input_passwd()
        passwd_field_label = RP.passwd_field_label()
        with assume:
            assert passwd_field_label.text == 'პაროლი'
        input_passwd.send_keys('Kekenadze2020')

    @allure.title("click submit button")
    @allure.description("when I go to the register page i should submit it")
    def test_click_reg_button_3(self):
        reg_button = RP.click_registration()
        with assume:
            assert reg_button.text == 'რეგისტრაცია'
        reg_button.click()

    @allure.title("check validations N3")
    @allure.description("when i submit my own datas, the website should send error messages")
    def test_check_valid_message_3(self):
        passwd_valid = RP.check_passwd_valid_mess()
        email_valid = RP.check_mail_valid_mess()
        re_pass_valid = RP.check_re_pass_valid_mess()
        terms_valid = RP.check_terms_valid_mess()

        with assume: assert email_valid.text == "ელ-ფოსტა ელ-ფოსტა ველში არასწორია."
        with assume: assert passwd_valid.text == "პაროლები ველებში დაადასტურეთ პაროლი და პაროლი ერთმანეთს არ ემთხვევა."
        with assume: assert re_pass_valid.text == "ველი დაადასტურეთ პაროლი აუცილებელია"
        with assume: assert terms_valid.text == "ველი დაეთანხმეთ საიტის მოხმარების წესებსა და პირობებს აუცილებელია"

    @allure.title("clear password field")
    @allure.description("when the test have done, i should clear the field of password")
    def test_clear_passwd_field(self):
        input_passwd = RP.input_passwd()
        input_passwd.clear()

    # TC4 Only Re-Password field is filled the rest is empty
    @allure.title("input registration re-password")
    @allure.description("when I go to the register page i should input re-password")
    def test_input_re_password(self):
        input_re_passwd = RP.input_re_passwd()
        re_passwd_field_label = RP.re_passwd_field_label()
        with assume:
            assert re_passwd_field_label.text == 'დაადასტურეთ პაროლი'
        input_re_passwd.send_keys('Kekenadze2020')

    @allure.title("click submit button")
    @allure.description("when I go to the register page i should submit it")
    def test_click_reg_button_5(self):
        reg_button = RP.click_registration()
        with assume:
            assert reg_button.text == 'რეგისტრაცია'
        reg_button.click()

    @allure.title("check validations N4")
    @allure.description("when i submit my own datas, the website should send error messages")
    def test_check_valid_message_4(self):
        passwd_valid = RP.check_passwd_valid_mess()
        email_valid = RP.check_mail_valid_mess()
        re_pass_valid = RP.check_re_pass_valid_mess()
        terms_valid = RP.check_terms_valid_mess()

        with assume: assert email_valid.text == "ელ-ფოსტა ელ-ფოსტა ველში არასწორია."
        with assume: assert passwd_valid.text == "ველი პაროლი აუცილებელია"
        with assume: assert re_pass_valid.text == "პაროლები ველებში პაროლი და პაროლი ერთმანეთს არ ემთხვევა."
        with assume: assert terms_valid.text == "ველი დაეთანხმეთ საიტის მოხმარების წესებსა და პირობებს აუცილებელია"

    @allure.title("clear password field")
    @allure.description("when the test have done, i should clear the field of password")
    def test_clear_re_passwd_field(self):
        input_re_passwd = RP.input_re_passwd()
        input_re_passwd.clear()
        time.sleep(3)

    # TC05 Only terms checkbox is marked

    @allure.title("mark checkbox")
    @allure.description("when I go to the register page i should mark checkbox")
    def test_check_box(self):
        check = RP.check_box()
        check_box_title = RP.check_box_title()
        with assume:
            assert check_box_title.text == 'დაეთანხმეთ საიტის მოხმარების წესებსა და პირობებს'
        check.click()

    @allure.title("click submit button")
    @allure.description("when I go to the register page i should submit it")
    def test_click_reg_button_6(self):
        reg_button = RP.click_registration()
        with assume:
            assert reg_button.text == 'რეგისტრაცია'
        reg_button.click()