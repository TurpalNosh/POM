import time

from pages.add_to_busk_page import AddBuskPage
from pages.login_page import LoginPage
from pages.check_out_page_step1 import CheckOutStep1
from pages.busket_page import BuskPage
from pages.check_out_page_step2 import CheckOutStep2
from pages.check_out_complete_page import CheckOutComplete

class TestSite:

    def setup_method(self):
        self.login_page = LoginPage(self.driver)
        self.add_to_busk = AddBuskPage(self.driver)
        self.busk_page = BuskPage(self.driver)
        self.check_out_step1 = CheckOutStep1(self.driver)
        self.check_out_step2 = CheckOutStep2(self.driver)
        self.check_out_complete = CheckOutComplete(self.driver)


    def test_login(self):
        self.login_page.open()
        self.login_page.enter_user_name("standard_user")
        self.login_page.enter_user_password("secret_sauce")
        self.login_page.login_button_click()

    def test_add_to_busk(self):
        self.add_to_busk.add_item_1()
        self.add_to_busk.add_item_2()
        self.add_to_busk.busk_button()

    def test_busk_page(self):
        self.busk_page.count_items()
        self.busk_page.check_out_button_click()

    def test_check_out_step1(self):
        self.check_out_step1.first_name_input("_")
        self.check_out_step1.last_name_input("_")
        self.check_out_step1.zip_input("_")

    def test_check_out_step2(self):
        self.check_out_step2.finish_button()

    def test_check_out_complete(self):
        self.check_out_complete.button_back_home()


