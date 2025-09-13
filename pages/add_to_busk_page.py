


from base.base_page import BasePage


class AddBuskPage(BasePage):

    _PAGE_URL = "https://www.saucedemo.com/inventory.html"

    _ITEM_1 = "//button[@id='add-to-cart-sauce-labs-backpack']"

    _ITEM_2 = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"

    _BUSK_BUTTON = "//a[@class='shopping_cart_link']"


    def add_item_1(self):
        self.driver.find_element(*self._ITEM_1).click()
    def add_item_2(self):
        self.driver.find_element(*self._ITEM_2).click()
    def busk_button(self):
        self.driver.find_element(*self._BUSK_BUTTON).click()


