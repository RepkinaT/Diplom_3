import allure

from locators import ResetPasswordLocators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = ResetPasswordLocators

    @allure.step('Ввести пароль')
    def enter_password(self):
        self.enter_data(self.locator.password_input, "password")

    @allure.step('Проверить тип поля для ввода пароля')
    def check_password_field_type(self):
        return self.get_element(self.locator.password_input).get_attribute('type')

    @allure.step('Нажать на значок видимости пароля')
    def click_password_visibility(self):
        self.click_element(self.locator.password_visibility)

    @allure.step('Получить текст кнопки "Сохранить"')
    def get_text_save_button(self):
        return self.get_text_element(self.locator.save_button)
