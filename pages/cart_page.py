from selenium.webdriver.common.by import By
import time


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def is_product_quantity_correct(self, expected_qty):
        try:
            qty_element = self.driver.find_element(By.XPATH, "//button[@class='disabled']")
            actual_qty = qty_element.text.strip()
            return str(expected_qty) == actual_qty
        except:
            return False
