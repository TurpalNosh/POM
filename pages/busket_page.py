
from base.base_page import BasePage

class BuskPage(BasePage):

    PAGE_URL = "https://www.saucedemo.com/cart.html"
    BUSK_BADGE = "//span[@class='shopping_cart_badge']"
    CHECK_OUT_BUTTON =  "//a[@class='shopping_cart_link']"


    def count_items(self):

        cart_badge = self.driver.find_element(*self.BUSK_BADGE)
        assert cart_badge.text == "2","в корзине два предмета"

    def check_out_button_click(self):
        self.driver.find_element(*self.CHECK_OUT_BUTTON).click()