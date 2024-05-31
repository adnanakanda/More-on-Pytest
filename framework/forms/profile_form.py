from forms.base_form import BaseForm
from browser.py_quality_services import PyQualityServices
from selenium.webdriver.common.by import By
from framework.locator_constants import LocatorConstant, ElementNameConstant
from core.elements.states.element_state_provider import ElementStateProvider



class ProfileForm(BaseForm):

    __page_name = "Albert Einstein"
    __tool_menu_btn = PyQualityServices.element_factory.get_button((By.XPATH,("//*[@id='vector-page-tools-dropdown']")),"Click tools")
    __download_lbl = PyQualityServices.element_factory.get_button((By.XPATH, LocatorConstant.PRECISE_TEXT_LOCATOR.format("Download as PDF")),"Click Download as PDF")
    def __init__(self):
        super(ProfileForm, self).__init__((By.XPATH, LocatorConstant.PRECISE_TEXT_LOCATOR.format(self.__page_name)), "Albert Einstein")


    def click_tool_menu(self):
        self.__tool_menu_btn.state.wait_for_clickable()
        self.__tool_menu_btn.click()


    def click_download_link(self):
        self.__download_lbl.state.wait_for_clickable()
        self.__download_lbl.click()