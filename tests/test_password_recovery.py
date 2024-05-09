import allure

from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage
from urls import login_url, forgot_url


class TestPasswordRecovery:
    @allure.title('Тест перехода на страницу восстановления пароля')
    @allure.description('Нажимаем на "Восстановить пароль" для перехода на нужную страницу. '
                        'Для определения того, что страница открылась правильная проверим наличие кнопки "Восстановить"')
    def test_go_to_the_password_recovery_page(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(login_url)
        login_page.click_restore_password()
        assert ForgotPasswordPage(driver).get_text_restore_button() == "Восстановить"

    @allure.title('Тест ввода email и нажатия на кнопку "Восстановить"')
    @allure.description('Вводим email и нажимаем кнопку "Восстановить". '
                        'Для определения того, что страница открылась правильная проверим наличие кнопки "Сохранить"')
    def test_entering_mail_and_pressing_button(self, driver, generate_random_email):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open_page(forgot_url)
        forgot_password_page.enter_email(generate_random_email)
        forgot_password_page.click_restore()
        assert ResetPasswordPage(driver).get_text_save_button() == "Сохранить"

    @allure.title('Тест кнопки показать/скрыть')
    @allure.description('Вводим пароль, нажимаем на кнопку видимости пароля и проверяем получим ли мы "text"')
    def test_show_hide_button_highlights_the_field(self, driver, generate_random_email):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open_page(forgot_url)
        forgot_password_page.enter_email(generate_random_email)
        forgot_password_page.click_restore()

        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.enter_password()
        reset_password_page.click_password_visibility()
        assert reset_password_page.check_password_field_type() == "text"
