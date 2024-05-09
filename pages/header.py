import allure

from locators import HeaderLocators
from pages.base_page import BasePage


class Header(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = HeaderLocators

    @allure.step('Нажать "Лента заказов"')
    def click_order_feed(self):
        self.click_element(self.locator.order_feed)

    @allure.step('Нажать "Конструктор"')
    def click_constructor(self):
        self.click_element(self.locator.constructor)
        self.wait_page_transition(self.locator.constructor)

    @allure.step('Нажать "Личный Кабинет"')
    def click_profile(self, wait_locator):
        self.click_element(self.locator.profile)
        self.wait_page_transition(wait_locator)
