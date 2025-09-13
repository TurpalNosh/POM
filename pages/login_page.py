import time

from base.base_page import BasePage


#класс страницы
class LoginPage(BasePage):
    # url страницы
    _PAGE_URL = "https://www.saucedemo.com"

    #Локаторы страницы
    _USER_NAME_FIELD = "//input[@id='user-name']"
    _LOGIN_FIELD = "//input[@id='login_email']"
    _USER_PASSWORD_FIELD = "//input[@id='password']"
    _LOGIN_BUTTON = "//input[@id='login-button']"

    def enter_user_name(self, user_name):
        self.driver.find_element(*self._USER_NAME_FIELD).send_keys(user_name)

    def enter_user_password(self, user_password):
        self.driver.find_element(*self._USER_PASSWORD_FIELD).send_keys(user_password)

    def login_button_click(self):
        self.driver.find_element(*self._LOGIN_BUTTON).click()
time.sleep(3)
