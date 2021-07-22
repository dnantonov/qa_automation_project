from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.is_element_present(*LoginPageLocators.LOGIN_URL), "Login url is not presented"
        assert "login" in self.browser.current_url, "There is not login in url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        register_email = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTER)
        register_email.send_keys(email)
        register_password = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTER)
        register_password.send_keys(password)
        register_password2 = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTER_REPEAT)
        register_password2.send_keys(password)
        register_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        register_btn.click()
