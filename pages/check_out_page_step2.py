

from base.base_page import BasePage


class CheckOutStep2(BasePage):

    _PAGE_URL = "https://www.saucedemo.com/checkout-step-two.html"
    _FINISH_BUTTON = "//button[@id ='finish']"

    def finish_button(self):
        self.driver.find_element(*self._FINISH_BUTTON).click()
