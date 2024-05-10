import allure

from locators import ConstructorPageLocators
from pages.base_page import BasePage


class ConstructorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = ConstructorPageLocators

    @allure.step('Нажать "Флюоресцентная булка R2-D3"')
    def click_first_bun(self):
        self.click_element(self.locator.first_bun)

    @allure.step('Получаем текст окна "Детали ингредиента"')
    def click_find_details(self):
        return self.get_text_element(self.locator.details_bun)

    @allure.step('Закрыть окно')
    def close_a_window(self):
        self.wait_element_invisibility()
        self.wait_element_visibility(self.locator.close_a_window)
        self.click_element(self.locator.close_a_window)

    @allure.step('Получаем название класса у модального окна')
    def get_text_class_section(self):
        return self.get_element_with_attribute(self.locator.third_section, "class")

    @allure.step('Добавить ингредиент в бургер')
    def move_ingredient_to_add_constructor(self):
        self.move_the_element(self.locator.first_bun, self.locator.ingredient_adding_area)

    @allure.step("Получаем количество добавленного ингредиента")
    def get_counter_ingredient(self):
        return self.get_text_element(self.locator.counter_ingredient)

    @allure.step('Нажимаем "Оформить заказ"')
    def click_create_order(self):
        self.click_element(self.locator.create_order)
        self.wait_page_transition(self.locator.create_order)

    @allure.step('Получаем идентификатор заказа')
    def get_modal_order_text(self):
        return self.get_text_element(self.locator.id_order)

    @allure.step("Получаем номер своего заказа")
    def get_number_order(self):
        self.wait_element_invisibility()
        return self.get_text_element(self.locator.number_order)

    @allure.step('Закрываем модальное окно созданного заказа')
    def click_close_modal_button(self):
        self.wait_element_visibility(self.locator.order_modal_opened)
        self.wait_element_invisibility(self.locator.order_modal_opened)
        self.click_element(self.locator.close_modal_button)
