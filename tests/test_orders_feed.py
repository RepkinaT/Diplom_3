import allure

from pages.constructor_page import ConstructorPage
from pages.header import Header
from pages.login_page import LoginPage
from pages.orders_feed_page import OrdersFeedPage
from pages.profile_page import ProfilePage
from pages.registration_page import RegistrationPage


class TestOrdersFeedPage:
    @allure.title('Тест открытия всплывающего окна детализации заказа')
    @allure.description('Проверяем открытие окна детализации, должны найти заголовок "Состав"')
    def test_opening_the_detail_window(self, driver):
        Header(driver).click_order_feed()
        page = OrdersFeedPage(driver)
        page.click_history_of_orders()

        assert page.get_composition_on_modal() == "Cостав"

    @allure.title('Тест отображения заказа пользователя в Ленте заказов')
    @allure.description('Регистрируем пользователя, создаем заказ и '
                        'проверяем отображения заказа пользователя в Ленте заказов, должны найти его номер')
    def test_check_user_order_in_the_feed(self, driver, generate_random_name, generate_random_email,
                                          generate_random_password):
        register_page = RegistrationPage(driver)
        register_page.registration_user(generate_random_name, generate_random_email,
                                        generate_random_password)
        login_page = LoginPage(driver)
        login_page.authorization_user(generate_random_email, generate_random_password)
        header = Header(driver)
        header.click_constructor()

        constructor_page = ConstructorPage(driver)
        constructor_page.move_ingredient_to_add_constructor()
        constructor_page.click_create_order()
        constructor_page.close_a_window()
        header.click_order_feed()

        feed_page = OrdersFeedPage(driver)
        feed_page.click_history_of_orders()
        id_order_feed = feed_page.get_id_on_modal()
        feed_page.click_close_modal_button()

        profile_page = ProfilePage(driver)
        header.click_profile(profile_page.locator.logout)
        profile_page.click_history_of_orders_view_list()
        first_order_id = profile_page.get_first_order_id()

        assert str(id_order_feed).strip() == str(first_order_id).strip()

    @allure.title('Тест увеличения счетчика заказов за все время, если добавить новый заказ')
    @allure.description("Регистрируем пользователя, создаем заказ и проверяем увеличился ли счетчик за все время")
    def test_increase_in_order_counter_for_all_time(self, driver, generate_random_name, generate_random_email,
                                                    generate_random_password):
        register_page = RegistrationPage(driver)
        register_page.registration_user(generate_random_name, generate_random_email,
                                        generate_random_password)
        login_page = LoginPage(driver)
        login_page.authorization_user(generate_random_email, generate_random_password)

        Header(driver).click_order_feed()

        orders_feed_page = OrdersFeedPage(driver)
        counter_before = orders_feed_page.get_all_time_order_counter()

        Header(driver).click_constructor()

        page = ConstructorPage(driver)
        page.move_ingredient_to_add_constructor()
        page.click_create_order()
        page.click_close_modal_button()

        Header(driver).click_order_feed()

        counter_after = orders_feed_page.get_all_time_order_counter()

        assert counter_after > counter_before

    @allure.title('Тест увеличения счетчика заказов за сегодня, если добавить новый заказ')
    @allure.description("Регистрируем пользователя, создаем заказ и проверяем увеличился ли счетчик за сегодня")
    def test_increase_in_order_counter_for_today(self, driver, generate_random_name, generate_random_email,
                                                 generate_random_password):
        register_page = RegistrationPage(driver)
        register_page.registration_user(generate_random_name, generate_random_email,
                                        generate_random_password)
        login_page = LoginPage(driver)
        login_page.authorization_user(generate_random_email, generate_random_password)

        Header(driver).click_order_feed()

        orders_feed_page = OrdersFeedPage(driver)
        counter_before = orders_feed_page.get_today_time_order_counter()

        Header(driver).click_constructor()

        page = ConstructorPage(driver)
        page.move_ingredient_to_add_constructor()
        page.click_create_order()
        order_number = page.get_number_order()
        page.close_a_window()

        Header(driver).click_order_feed()
        counter_after = orders_feed_page.get_today_time_order_counter_after(order_number)

        assert counter_after > counter_before

    @allure.title('Тест появления нового заказа в разделе "В работе"')
    @allure.description("Регистрируем пользователя, создаем заказ и проверяем появления нового заказа в нужном разделе")
    def test_check_the_new_order_in_work(self, driver, generate_random_name, generate_random_email,
                                         generate_random_password):
        register_page = RegistrationPage(driver)
        register_page.registration_user(generate_random_name, generate_random_email,
                                        generate_random_password)
        login_page = LoginPage(driver)
        login_page.authorization_user(generate_random_email, generate_random_password)

        Header(driver).click_constructor()

        page = ConstructorPage(driver)
        page.move_ingredient_to_add_constructor()
        page.click_create_order()
        order_number = page.get_number_order()
        page.close_a_window()

        Header(driver).click_order_feed()

        orders_feed_page = OrdersFeedPage(driver)
        order_number_ = orders_feed_page.get_orders_in_work(order_number)

        assert (6 - len(order_number)) * "0" + order_number == order_number_
