from base.base_page import BasePage

class CheckOutComplete(BasePage):

    _PAGE_URL = "https://www.saucedemo.com/checkout-complete.html"
    _BACK_HOME_BUTTON = "//button[@id ='back-to-products']"

    def button_back_home(self):
        self.driver.find_element(*self._BACK_HOME_BUTTON).click()
