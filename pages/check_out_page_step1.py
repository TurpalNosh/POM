

from base.base_page import BasePage


class CheckOutStep1(BasePage):
    _PAGE_URL="https://www.saucedemo.com/checkout-step-one.html"
    _FIRST_NAME_INPUT = "//input[@id='first-name']"
    _LAST_NAME_INPUT = "//input[@id='last-name']"
    _BUTTON_CONTINUE = "//input[@id='continue']"
    _ZIP_INPUT = "//input[@id='postal-code']"

    def first_name_input(self,first_name):
        self.driver.find_element(*self._FIRST_NAME_INPUT).send_keys(first_name)

    def last_name_input(self,last_name):
        self.driver.find_element(*self._LAST_NAME_INPUT).send_keys(last_name)
    def zip_input(self,zip):
        self.driver.find_element(*self._ZIP_INPUT).send_keys(zip)

    def button_continue(self):
        self.driver.find_element(*self._BUTTON_CONTINUE).click()





