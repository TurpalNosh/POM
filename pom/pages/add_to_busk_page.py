

from selenium.webdriver.support import expected_conditions as EC
from pom.base.base_page import BasePage



class AddBuskPage(BasePage):

    _PAGE_URL = "https://www.saucedemo.com/inventory.html"

    _ITEM_1 = "xpath","//button[@id='add-to-cart-sauce-labs-backpack']"

    _ITEM_2 = "xpath","//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"

    _BUSK_BUTTON = "xpath","//a[@class='shopping_cart_link']"

    _CHECK_OUT_BUTTON = "xpath","//button[@id='checkout']"


    def add_item_1(self):
        self.wait.until(EC.element_to_be_clickable(self._ITEM_1)).click()
    def add_item_2(self):
       self.wait.until(EC.element_to_be_clickable(self._ITEM_2)).click()
    def busk_button(self):
       self.wait.until(EC.element_to_be_clickable(self._BUSK_BUTTON)).click()
    #def check_out_button(self):
        #self.wait.until(EC.element_to_be_clickable(self._CHECK_OUT_BUTTON)).click()


    # def add_item_1(self):
    #     self.wait_for_element_clickable(self._ITEM_1).click()
    #
    # def add_item_2(self):
    #     self.wait_for_element_clickable(self._ITEM_2).click()
    #
    # def busk_button(self):
    #     self.wait_for_element_clickable(self._BUSK_BUTTON).click()


