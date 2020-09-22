from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    EMAIL_LOGIN = (By.CSS_SELECTOR, "#id_login-username")
    PASSWORD_LOGIN = (By.CSS_SELECTOR, "#id_login-password")

    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_BTN = (By.CSS_SELECTOR, 'button[name="registration_submit"]')
    EMAIL_REGISTER = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_REGISTER = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_REGISTER_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")


class ProductPageLocators():
    CART_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    PRODUCT_LINK = (By.CSS_SELECTOR, "div.basket-items a")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")