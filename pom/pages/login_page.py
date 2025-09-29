
import allure
from pom.base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC




class LoginPage(BasePage):
    _PAGE_URL = "https://www.saucedemo.com"
    _USER_NAME_FILED = "xpath","//input[@id='user-name']"
    _USER_PASSWORD = "xpath","//input[@id='password']"
    _BUTTON_LOGIN = "xpath","//input[@id='login-button']"
    @allure.step("enter  login")
    def enter_user_name(self, user_name):
        self.wait.until(EC.element_to_be_clickable(self._USER_NAME_FILED)).send_keys(user_name)


    @allure.step("enter  password")
    def enter_user_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self._USER_PASSWORD)).send_keys(password)


    @allure.step("click button login")
    def button_login(self):
        self.wait.until(EC.element_to_be_clickable(self._BUTTON_LOGIN)).click()
