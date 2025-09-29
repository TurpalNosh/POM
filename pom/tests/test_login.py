
from pom.pages.add_to_busk_page import AddBuskPage
from pom.pages.login_page import LoginPage
from pom.pages.check_out_page_step1 import CheckOutStep1
from pom.pages.busket_page import BuskPage
from pom.pages.check_out_page_step2 import CheckOutStep2
from pom.pages.check_out_complete_page import CheckOutComplete

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
        self.login_page.button_login()

        self.add_to_busk.add_item_1()
        self.add_to_busk.add_item_2()
        self.add_to_busk.busk_button()

        self.busk_page.count_items()
        self.busk_page.check_out_button_click()



        self.check_out_step1.first_name_input("Фрунзик")
        self.check_out_step1.last_name_input("Кулимпаторский")
        self.check_out_step1.zip_input("333")
        self.check_out_step1.button_continue()

        self.check_out_step2.finish_button()

        self.check_out_complete.button_back_home()



