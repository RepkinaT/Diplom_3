import allure

from locators import ProfilePageLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = ProfilePageLocators

    @allure.step('Нажать "История заказов"')
    def click_history_of_orders(self):
        self.click_element(self.locator.history_of_orders)
        self.wait_page_transition(self.locator.logout)

    @allure.step('Нажать "История заказов" для просмотра списка заказов')
    def click_history_of_orders_view_list(self):
        self.wait_element_invisibility()
        self.click_element(self.locator.history_of_orders)
        self.wait_page_transition(self.locator.first_order_id)

    @allure.step('Нажать "История заказов"')
    def get_first_order_id(self):
        self.get_text_element(self.locator.first_order_id)

    @allure.step('Нажать "Выход"')
    def click_logout(self):
        self.click_element(self.locator.logout)
