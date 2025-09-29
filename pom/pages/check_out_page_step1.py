

from pom.base.base_page import BasePage


class CheckOutStep1(BasePage):
    _PAGE_URL="https://www.saucedemo.com/checkout-step-one.html"
    _FIRST_NAME_INPUT = "xpath","//input[@name='firstName']"
    _LAST_NAME_INPUT = "xpath","//input[@id='last-name']"
    _BUTTON_CONTINUE = "xpath","//input[@id='continue']"
    _ZIP_INPUT = "xpath","//input[@id='postal-code']"

    def first_name_input(self,first_name):
        self.driver.find_element(*self._FIRST_NAME_INPUT).send_keys(first_name)
        assert self.driver.current_url == "https://www.saucedemo.com/checkout-step-one.html", f"мы на странице чек аута"  # проверка что мы провалились в чекаут

    def last_name_input(self,last_name):
        self.driver.find_element(*self._LAST_NAME_INPUT).send_keys(last_name)
    def zip_input(self,zip):
        self.driver.find_element(*self._ZIP_INPUT).send_keys(zip)

    def button_continue(self):
        self.driver.find_element(*self._BUTTON_CONTINUE).click()

    # def first_name_input(self, first_name):
    #     self.wait_for_element_clickable(self._FIRST_NAME_INPUT).send_keys(first_name)
    #
    # def last_name_input(self, last_name):
    #     self.wait_for_element_clickable(self._LAST_NAME_INPUT).send_keys(last_name)
    #
    # def zip_input(self, zip):
    #     self.wait_for_element_clickable(self._ZIP_INPUT).send_keys(zip)
    #
    # def button_continue(self):
    #     self.wait_for_element_clickable(self._BUTTON_CONTINUE).click()



