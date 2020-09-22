import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.base_page import BasePage


@pytest.mark.login_guest
class TestLoginFromMainPage():
   def test_guest_can_go_to_login_page(self, browser): 
      link = "http://selenium1py.pythonanywhere.com"
      page = MainPage(browser, link)
      page.open()
      page.go_to_login_page()
      login_page = LoginPage(browser, browser.current_url)
      login_page.should_be_login_page()

   def test_guest_should_see_login_link(self, browser):
      link = "http://selenium1py.pythonanywhere.com"
      page = MainPage(browser, link)
      page.open()
      page.should_be_login_link()




# def test_guest_can_go_to_login_page(browser): 
#       link = "http://selenium1py.pythonanywhere.com"
#       page = MainPage(browser, link)
#       page.open()
#       page.go_to_login_page()
#       login_page = LoginPage(browser, browser.current_url)
#       login_page.should_be_login_page()


# def test_guest_should_see_login_link(browser):
#    link = "http://selenium1py.pythonanywhere.com"
#    page = MainPage(browser, link)
#    page.open()
#    page.should_be_login_link()


# def go_to_login_page(self):
#    link = self.browser.find_element_by_css_selector("#login_link")
#    link.click()
#    alert = self.browser.switch_to.alert
#    alert.accept()


# @pytest.mark.skip
# def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
#    link = "http://selenium1py.pythonanywhere.com"
#    page = BasketPage(browser, link)
#    page.open()
#    page.go_to_basket_page()
#    page.should_not_be_products_in_basket()
#    page.should_be_message_about_basket_is_empty()