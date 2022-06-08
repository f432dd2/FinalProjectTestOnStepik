from lib2to3.pgen2 import driver
from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "[href=\"/ru/accounts/login/\"]")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class AddToBasket():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "[class\"btn btn-lg btn-primary btn-add-to-basket\"]")