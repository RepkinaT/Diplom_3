import allure

from helpers import RandomData
from pages.constructor_page import ConstructorPage
from pages.header import Header
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from urls import order_feed_url, main_url


class TestMainPage:
    @allure.title('Тест перехода на страницу Конструктор')
    @allure.description('Нажимаем на "История заказов" с главной страницы, '
                        'затем переходим на страницу Конструктор по кнопке в меню')
    def test_transition_constructor(self, driver):
        page = Header(driver)
        page.click_order_feed()
        page.click_constructor()

        assert page.get_current_url == main_url

    @allure.title('Тест перехода на страницу История заказов')
    @allure.description('Нажимаем на "История заказов" в меню с главной страницы')
    def test_transition_order_feed(self, driver):
        page = Header(driver)
        page.click_order_feed()

        assert page.get_current_url == order_feed_url

    @allure.title('Тест открытия всплывающего окна с ингредиентами')
    @allure.description('Нажимаем на булку, чтобы посмотреть детали ингредиента')
    def test_open_window_with_ingredients(self, driver):
        page = ConstructorPage(driver)
        page.click_first_bun()

        assert page.click_find_details() == "Детали ингредиента"

    @allure.title('Тест закрытия всплывающего окна с ингредиентами')
    @allure.description('Нажимаем на булку, чтобы посмотреть детали ингредиента и закрываем окно')
    def test_close_window_with_ingredients(self, driver):
        page = ConstructorPage(driver)
        page.click_first_bun()
        page.close_a_window()

        assert page.get_text_class_section().startswith("Modal_modal_opened") is False

    @allure.title('Тест увеличения счетчика ингредиентов')
    @allure.description("Нажимаем на булку и переносим ее в конструктор бургера, значение счетчика должно стать 2")
    def test_increasing_ingredient_counter(self, driver):
        page = ConstructorPage(driver)
        page.move_ingredient_to_add_constructor()
        counter = page.get_counter_ingredient()

        assert counter == "2"

    @allure.title('Тест создания заказа авторизованным пользователем')
    @allure.description("Проходим регистрацию и создаем заказ, проверяем по тексту 'идентификатор заказа'")
    def test_create_order_authorized_user(self, driver):
        name = RandomData.generate_random_name()
        email = RandomData.generate_random_email()
        password = RandomData.generate_random_password()
        register_page = RegistrationPage(driver)
        register_page.registration_user(name, email, password)
        login_page = LoginPage(driver)
        login_page.authorization_user(email, password)
        Header(driver).click_constructor()

        page = ConstructorPage(driver)
        page.move_ingredient_to_add_constructor()
        page.click_create_order()

        assert page.get_modal_order_text() == "идентификатор заказа"
