from selenium.webdriver.common.by import By


class Locators:
    #MainPageLocators
    reg_button_xpath = (By.XPATH, '//*[@id="tygh_main_container"]/div[2]/div/div[2]/div/div/div/div/div[2]/div['
                                  '1]/a/span/b')

    reg_title_xpath= (By.XPATH, '//*[@id="login_block342"]/div/div/div[3]/div[1]/a')


    #RegistrationPageLocators

    email_field_ID = (By.ID,'email')