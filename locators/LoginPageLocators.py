from selenium.webdriver.common.by import By


class LoginLocator:
    Login_field_ID = (By.ID, 'login_popup175')

    paswd_field_ID = (By.ID, 'psw_popup175')

    login_button_modal = (By.XPATH, '//*[@id="tab_login"]/form/div[3]/button')
