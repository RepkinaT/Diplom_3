from selenium.webdriver.common.by import By


class LocatorGeneral:
    modal_window = By.XPATH, "//div[contains(@class, 'Modal_modal__P3_V5')]//div"


class HeaderLocators:
    constructor = By.XPATH, './/p[text()="Конструктор"]'
    order_feed = By.XPATH, './/p[text()="Лента Заказов"]'
    profile = By.XPATH, './/p[text()="Личный Кабинет"]'


class ConstructorPageLocators:
    first_bun = By.XPATH, './/p[text()="Флюоресцентная булка R2-D3"]'
    details_bun = By.XPATH, './/h2[text()="Детали ингредиента"]'
    close_a_window = By.XPATH, './/button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]'
    third_section = By.XPATH, "(//section)[3]"
    ingredient_adding_area = By.XPATH, './/section[contains(@class, "BurgerConstructor_basket")]'
    counter_ingredient = By.XPATH, first_bun[1] + "/../div/p"
    create_order = By.XPATH, './/button[text()="Оформить заказ"]'
    id_order = By.XPATH, './/p[text()="идентификатор заказа"]'
    number_order = By.XPATH, './/h2[contains(@class, "title_shadow__3ikwq")]'
    order_modal_opened = By.XPATH, './/div[contains(@class, "Modal_modal_opened__3ISw4")]'
    close_modal_button = By.XPATH, '(.//div[contains(@class, "Modal_modal__container__Wo2l_")])[1]//button'


class OrdersFeedPageLocators:
    first_order = By.XPATH, '(.//div[contains(@class, "OrderFeed_contentBox__3-tWb")]//ul//li)[1]'
    composition = By.XPATH, './/p[text()="Cостав"]'
    id_order = By.XPATH, './/p[contains(@class, "text text_type_digits-default mb-10 mt-5")]'
    order_modal_opened = By.XPATH, './/div[contains(@class, "Modal_modal_opened__3ISw4")]'
    close_modal_button = By.XPATH, '(.//div[contains(@class, "Modal_modal__container__Wo2l_")])[2]//button'
    counter_all_time = By.XPATH, '(.//p[contains(@class, "OrderFeed_number__2MbrQ")])[1]'
    counter_today = By.XPATH, '(.//p[contains(@class, "OrderFeed_number__2MbrQ")])[last()]'
    counter_today_after = [By.XPATH, '(.//p[contains(@class, "OrderFeed_number__2MbrQ")])[last()][text()="{value}"]']
    orders_in_work = [By.XPATH,
                      "//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li[text()='{value}']"]
    all_orders_complete = By.XPATH, './/li[text()="Все текущие заказы готовы!"]'


class LoginPageLocators:
    email_input = By.XPATH, './/input[@name="name"]'
    password_input = By.XPATH, './/input[@name="Пароль"]'
    login_button = By.XPATH, './/button[text()="Войти"]'
    restore_password = By.XPATH, './/a[text()="Восстановить пароль"]'


class LocatorRegistration:
    name_input = By.XPATH, "//label[text()='Имя']/../input"
    email_input = By.XPATH, "//label[text()='Email']/../input"
    password_input = By.XPATH, "//label[text()='Пароль']/../input"

    submit_button = By.XPATH, './/button[text()="Зарегистрироваться"]'


class ProfilePageLocators:
    history_of_orders = By.XPATH, './/a[text()="История заказов"]'
    logout = By.XPATH, './/button[text()="Выход"]'
    first_order_id = By.XPATH, '((.//div[contains(@class, "OrderHistory_orderHistory__qy1VB")]//ul//li)[1]//p)[1]'


class ForgotPasswordLocators:
    email_input = By.XPATH, './/input[@name="name"]'
    restore_button = By.XPATH, './/button[text()="Восстановить"]'
    save_button = By.XPATH, './/button[text()="Сохранить"]'


class ResetPasswordLocators:
    password_input = By.XPATH, './/label[text()="Пароль"]/parent::div/input'
    password_visibility = By.XPATH, './/div[@class="input__icon input__icon-action"]'
    save_button = By.XPATH, './/button[text()="Сохранить"]'
