import allure

from locators import OrdersFeedPageLocators
from pages.base_page import BasePage


class OrdersFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = OrdersFeedPageLocators

    @allure.step('Нажать на первый заказ в ленте')
    def click_history_of_orders(self):
        self.click_element(self.locator.first_order)

    @allure.step('Получить "Состав" из модального окна')
    def get_composition_on_modal(self):
        return self.get_text_element(self.locator.composition)

    @allure.step('Получить ID заказа')
    def get_id_on_modal(self):
        return self.click_element(self.locator.id_order)

    @allure.step('Закрыть модальное окно')
    def click_close_modal_button(self):
        self.click_element(self.locator.close_modal_button)

    @allure.step('Получить значение счетчика заказов за все время')
    def get_all_time_order_counter(self):
        self.wait_page_transition(self.locator.first_order)
        result = self.get_text_element(self.locator.counter_all_time)
        return result

    @allure.step('Получить значение счетчика заказов за сегодня до создания заказа')
    def get_today_time_order_counter(self):
        self.wait_page_transition(self.locator.first_order)
        result = self.get_text_element(self.locator.counter_today)
        return result

    @allure.step('Получить значение счетчика заказов за сегодня после создания заказа')
    def get_today_time_order_counter_after(self, value):
        self.locator.orders_in_work.append(self.locator.orders_in_work.pop().format(value=value))
        self.wait_page_transition(self.locator.orders_in_work)
        result = self.get_text_element(self.locator.counter_today)
        return result

    @allure.step('Получить заказ "В работе"')
    def get_orders_in_work(self, value):
        self.locator.orders_in_work.append(self.locator.orders_in_work.pop().format(value=value))
        self.wait_page_transition(self.locator.orders_in_work)  # Ожидаем элемент с определенным числом в li
        result = self.get_text_element(self.locator.orders_in_work)
        return result
