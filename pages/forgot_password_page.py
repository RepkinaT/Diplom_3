import allure

from locators import ForgotPasswordLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = ForgotPasswordLocators

    @allure.step('Ввести email')
    def enter_email(self, email):
        self.enter_data(self.locator.email_input, email)

    @allure.step('Нажать кнопку "Восстановить"')
    def click_restore(self):
        self.click_element(self.locator.restore_button)
        self.wait_page_transition(self.locator.save_button)

    @allure.step('Получить текст кнопки "Восстановить"')
    def get_text_restore_button(self):
        return self.get_text_element(self.locator.restore_button)
