from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Driver:
    """
        this is the configuration of driver
    """
    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Chrome("chromedriver",options=options)
    driver.maximize_window()
    # driver.set_window_size(1440, 768)
    driver.get("https://alta.ge/")
    driver.implicitly_wait(10)
