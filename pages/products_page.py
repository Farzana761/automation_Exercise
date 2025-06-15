from selenium.webdriver.common.by import By
import time


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    def click_view_product(self):
        view_buttons = self.driver.find_elements(By.XPATH, "//a[contains(text(),'View Product')]")
        if view_buttons:
            view_buttons[0].click()
            time.sleep(1)

    def is_product_detail_visible(self):
        return "product-details" in self.driver.page_source

    def set_quantity(self, qty):
        qty_box = self.driver.find_element(By.ID, "quantity")
        qty_box.clear()
        qty_box.send_keys(str(qty))

    def add_to_cart(self):
        # click add to cart button
        add_btn = self.driver.find_element(By.XPATH, "//button[normalize-space()='Add to cart']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", add_btn)
        add_btn.click()
        time.sleep(2)

        # modal popup and click 'View Cart'
        view_cart_btn = self.driver.find_element(By.XPATH, "//u[contains(text(),'View Cart')]")
        view_cart_btn.click()
        time.sleep(2)

    def view_cart(self):
        self.driver.find_element(By.XPATH, "//a[@href='/view_cart']").click()
        time.sleep(2)

    def search_product(self, product_name):
        search_input = self.driver.find_element(By.ID, "search_product")
        search_input.clear()
        search_input.send_keys(product_name)
        self.driver.find_element(By.ID, "submit_search").click()
        time.sleep(2)

    def get_search_results(self):
        return self.driver.find_elements(By.XPATH, "//div[@class='productinfo text-center']")
