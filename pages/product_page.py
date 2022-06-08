from .base_page import BasePage
from .locators import AddToBasket
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def add_poduct_to_basket(self):
        link = self.browser.find_element(*AddToBasket.ADD_TO_BASKET)
        link.click
        alert = self.browser.switch_to.alert
        alert.accept()

