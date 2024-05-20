from forms.base_form import BaseForm
from browser.py_quality_services import PyQualityServices
from selenium.webdriver.common.by import By
from framework.locator_constants import LocatorConstant, ElementNameConstant


class MainForm(BaseForm):
    def __init__(self):
        super(MainForm, self).__init__((By.XPATH, LocatorConstant.PRECISE_TEXT_LOCATOR.format("Welcome to the-internet")), "Main page")

    def get_navigation_link(self, navigation):
        # Return the navigation link element
        return PyQualityServices.element_factory.get_link((By.XPATH, LocatorConstant.PRECISE_TEXT_LOCATOR.format(navigation)), "Navigation link")

    def click_navigation_link(self, navigation):
        # Click the navigation link
        self.get_navigation_link(navigation).click()