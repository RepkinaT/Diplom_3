import allure

from locators import LocatorRegistration
from pages.base_page import BasePage
from urls import register_url


class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = LocatorRegistration

    @allure.step('Ввести имя')
    def enter_name(self, name):
        self.enter_data(self.locator.name_input, name)

    @allure.step('Ввести email')
    def enter_email(self, email):
        self.enter_data(self.locator.email_input, email)

    @allure.step('Ввести пароль')
    def enter_password(self, password):
        self.enter_data(self.locator.password_input, password)

    @allure.step('Нажать "Зарегистрироваться"')
    def click_login_button(self):
        self.click_element(self.locator.submit_button)

    @allure.step('Регистрация пользователя')
    def registration_user(self, name, email, password):
        self.open_page(register_url)
        self.enter_name(name)
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
