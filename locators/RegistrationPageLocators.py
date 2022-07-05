from selenium.webdriver.common.by import By

class RegistrationLocator:
    # RegistrationPageLocators
    email_field_label_xpath = (
        By.XPATH, '//*[@id="tygh_main_container"]/div[4]/div/div/div[2]/div/div/div/form/div[2]/label')
    email_field_ID = (By.ID, 'email')

    passwd_field_label_xpath = (
        By.XPATH, '//*[@id="tygh_main_container"]/div[4]/div/div/div[2]/div/div/div/form/div[3]/label')
    passwd_field_ID = (By.ID, 'password1')

    re_passwd_field_label_xpath = (
        By.XPATH, '//*[@id="tygh_main_container"]/div[4]/div/div/div[2]/div/div/div/form/div[4]/label')
    re_passwd_field_ID = (By.ID, 'password2')

    name_field_label_xpath = (
        By.XPATH, '//*[@id="tygh_main_container"]/div[4]/div/div/div[2]/div/div/div/form/div[5]/div[1]/label')
    name_field_ID = (By.ID, 'elm_6')

    surname_field_label_xpath = (
        By.XPATH, '//*[@id="tygh_main_container"]/div[4]/div/div/div[2]/div/div/div/form/div[5]/div[2]/label')
    surname_field_ID = (By.ID, "elm_7")

    check_box_title_xpath = (
        By.XPATH, '//*[@id="tygh_main_container"]/div[4]/div/div/div[2]/div/div/div/form/div[6]/label/a/b')
    check_box_ID = (By.ID, "id_accept_terms_site")

    registration_button_xpath = (
        By.XPATH, '//*[@id="tygh_main_container"]/div[4]/div/div/div[2]/div/div/div/form/div[7]/button')
