from forms.base_form import BaseForm
from browser.py_quality_services import PyQualityServices
from selenium.webdriver.common.by import By
from framework.locator_constants import LocatorConstant, ElementNameConstant
from core.elements.states.element_state_provider import ElementStateProvider



class FileDownloadForm(BaseForm):

    __page_name = "Download as PDF"
    __pdf_title = PyQualityServices.element_factory.get_button((By.XPATH,("//div[contains(@class, 'mw-electronpdfservice-selection-label-desc')]")),"File name")
    __download_btn = PyQualityServices.element_factory.get_button((By.XPATH,("//button[contains(@class, 'oo-ui-inputWidget-input')]")),"Download button")
    def __init__(self):
        super(FileDownloadForm, self).__init__((By.XPATH, LocatorConstant.PRECISE_TEXT_LOCATOR.format(self.__page_name)), "Albert Einstein")


    def get_pdf_name(self) -> str:
        return self.__pdf_title


    def download_file(self):
        self.__download_btn.click()


    def is_file_download_link_displayed(self, name):
        return self.__pdf_title.state.is_displayed