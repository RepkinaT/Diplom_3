import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import LocatorGeneral


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидаем сокрытия элемента')
    def wait_element_invisibility(self, wait_locator=LocatorGeneral.modal_window):
        element = self.driver.find_element(*wait_locator)
        WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located(element))

    @allure.step('Ожидаем видимости элемента')
    def wait_element_visibility(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))

    @allure.step('Ожидаем загрузки элемента')
    def wait_page_transition(self, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    @allure.step('Открываем страницу')
    def open_page(self, link):
        self.driver.get(link)
        self.wait_element_invisibility()

    @allure.step('Находим элемент')
    def get_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Получаем атрибут найденного элемента')
    def get_element_with_attribute(self, locator, value):
        return self.driver.find_element(*locator).get_attribute(value)

    @allure.step('Кликаем по элементу')
    def click_element(self, locator):
        self.get_element(locator).click()
        self.wait_element_invisibility()

    @allure.step('Получаем текст элемента')
    def get_text_element(self, locator):
        element = self.get_element(locator)
        return element.text

    @allure.step('Вносим данные в поле')
    def enter_data(self, locator, data):
        element = self.get_element(locator)
        element.send_keys(data)

    @allure.step('Перемещаем элемент')
    def move_the_element(self, locator_element, locator_target):
        element = self.get_element(locator_element)
        target = self.get_element(locator_target)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(element, target).perform()
