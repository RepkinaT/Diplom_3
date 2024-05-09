import allure

from locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = LoginPageLocators

    @allure.step('Ввести email')
    def enter_email(self, email):
        self.enter_data(self.locator.email_input, email)

    @allure.step('Ввести пароль')
    def enter_password(self, password):
        self.enter_data(self.locator.password_input, password)

    @allure.step('Нажать "Войти"')
    def click_login_button(self):
        self.click_element(self.locator.login_button)
        self.wait_page_transition(self.locator.login_button)

    @allure.step('Нажать "Восстановить пароль"')
    def click_restore_password(self):
        self.click_element(self.locator.restore_password)

    @allure.step('Авторизация пользователя')
    def authorization_user(self, email, password):
        self.wait_page_transition(self.locator.login_button)
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    @allure.step('Ожидаем выход с аккаунта')
    def wait_logout(self):
        self.wait_page_transition(self.locator.login_button)
