from metaclasses.meta_locator import MetaLocator
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.select import Select
import time


class BasePage(metaclass=MetaLocator):


    def __init__(self, driver):
        self.driver:WebDriver = driver

    def open(self):
        self.driver.get(self._PAGE_URL)

