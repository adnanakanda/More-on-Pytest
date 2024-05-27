from forms.base_form import BaseForm
from browser.py_quality_services import PyQualityServices
from selenium.webdriver.common.by import By
from framework.locator_constants import LocatorConstant, ElementNameConstant



class Wiki_MainForm(BaseForm):

    __search_field = PyQualityServices.element_factory.get_text_box((By.XPATH, "//input[@id='searchInput']"), "Search Input")
    __search_button = PyQualityServices.element_factory.get_button((By.XPATH, "//button[contains(@class, 'pure-button-primary-progressive')]"),"Click search button")
    def __init__(self):
        super(Wiki_MainForm, self).__init__((By.XPATH, LocatorConstant.PRECISE_TEXT_LOCATOR.format("The Free Encyclopedia")), "Wikipedia home page")

    def get_navigation_link(self, navigation):
        # Return the navigation link element
        return PyQualityServices.element_factory.get_link((By.XPATH, LocatorConstant.PRECISE_TEXT_LOCATOR.format(navigation)), "Navigation link")

    def click_navigation_link(self, navigation):
        # Click the navigation link
        self.get_navigation_link(navigation).click()

    def is_main_page_displayed(self, navigation_name):
        navigation_link = self.get_navigation_link(navigation_name)
        return navigation_link.state.is_displayed


    def search_text(self, name):
        self.__search_field.clear_and_type(name)


    def click_search_btn(self):
        #assert self.__search_button is not None, "Search button was not found"
        self.__search_button.click()