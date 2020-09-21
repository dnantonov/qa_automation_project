from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_cart(self):
        self.should_be_cart_button()
        self.find_cart_button_and_click()
        self.solve_quiz_and_get_code()
        self.added_product_check()

    def find_cart_button_and_click(self):
        link = self.browser.find_element(*ProductPageLocators.CART_BUTTON)
        link.click()

    def should_be_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.CART_BUTTON), "Cart button is not presented"

    def added_product_check(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_added_name = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED).text
        assert product_name == product_added_name, "Items don't the same"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"
    
    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"
    