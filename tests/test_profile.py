import allure

from helpers import RandomData
from locators import ProfilePageLocators, LoginPageLocators
from pages.header import Header
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.registration_page import RegistrationPage
from urls import login_url, history_url


class TestProfilePage:
    @allure.title('Тест перехода на страницу Личного кабинета')
    @allure.description('Нажимаем на "Личный кабинет" с главной страницы')
    def test_transition_profile_page(self, driver):
        page = Header(driver)
        page.click_profile(LoginPageLocators.login_button)

        assert page.get_current_url == login_url

    @allure.title('Тест перехода на страницу История заказов')
    @allure.description('Нажимаем на "История заказов" с главной страницы')
    def test_transition_history_order(self, driver):
        header = Header(driver)

        name = RandomData.generate_random_name()
        email = RandomData.generate_random_email()
        password = RandomData.generate_random_password()
        register_page = RegistrationPage(driver)
        register_page.registration_user(name, email, password)
        login_page = LoginPage(driver)
        login_page.authorization_user(email, password)

        profile_page = ProfilePage(driver)
        header.click_profile(ProfilePageLocators.logout)
        profile_page.click_history_of_orders()
        assert profile_page.get_current_url == history_url

    @allure.title('Тест выхода из аккаунта')
    @allure.description('Нажимаем на "Личный кабинет" регистрируемся и выходим из аккаунта')
    def test_logout_profile(self, driver):
        header = Header(driver)
        name = RandomData.generate_random_name()
        email = RandomData.generate_random_email()
        password = RandomData.generate_random_password()
        register_page = RegistrationPage(driver)
        register_page.registration_user(name, email, password)
        login_page = LoginPage(driver)
        login_page.authorization_user(email, password)

        profile_page = ProfilePage(driver)
        header.click_profile(ProfilePageLocators.logout)
        profile_page.click_logout()
        login_page.wait_logout()

        assert profile_page.get_current_url == login_url
