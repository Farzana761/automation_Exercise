import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_add_product_to_cart(driver):
    driver.get("https://automationexercise.com")
    time.sleep(2)
    assert "Automation Exercise" in driver.title

    home = HomePage(driver)
    home.go_to_products()
    time.sleep(2)

    product_page = ProductsPage(driver)
    product_page.click_view_product()
    assert product_page.is_product_detail_visible(), "Product detail page not visible"

    product_page.set_quantity(4)
    product_page.add_to_cart()
    product_page.view_cart()

    cart = CartPage(driver)
    assert cart.is_product_quantity_correct(4), "Product quantity is incorrect in cart"


def test_search_product(driver):
    driver.get("https://automationexercise.com")
    time.sleep(2)
    assert "Automation Exercise" in driver.title

    home = HomePage(driver)
    home.go_to_products()
    time.sleep(2)

    products = ProductsPage(driver)
    products.search_product("Tshirt")
    time.sleep(2)

    results = products.get_search_results()
    assert len(results) > 0, "No products found for the search keyword"
