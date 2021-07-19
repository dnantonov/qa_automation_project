## Финальный проект курса Степик: Автоматизированной тестирование с Selenium и Python

Technologies: Python, Selenium, pytest

Для запуска тестов необходимо установить пакеты следующей командой:

`pip install -r requirements.txt`

#### Запуск тестов:

`pytest test_main_page.py`

Включает в себя следующие тест-кейсы:

- test_guest_can_go_to_login_page
- test_guest_should_see_login_link
- go_to_login_page
- test_guest_cant_see_product_in_basket_opened_from_main_page
- test_guest_can_go_to_login_page
- test_guest_should_see_login_link

`pytest test_product_page.py`

Включает в себя следующие тест-кейсы:

- test_guest_can_add_product_to_basket
- test_message_disappeared_after_adding_product_to_basket
- test_guest_should_see_login_link_on_product_page
- test_guest_can_go_to_login_page_from_product_page
- test_guest_cant_see_product_in_basket_opened_from_product_page
- test_user_cant_see_success_message
- test_user_can_add_product_to_basket

