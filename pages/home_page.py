from selenium.webdriver.common.by import By
import time


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_products(self):
        products_btn = self.driver.find_element(By.XPATH, "//a[@href='/products']")
        products_btn.click()
        time.sleep(1)

    def is_home_visible(self):
        return "Home" in self.driver.page_source
