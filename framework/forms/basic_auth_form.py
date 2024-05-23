from forms.base_form import BaseForm
from browser.py_quality_services import PyQualityServices
from selenium.webdriver.common.by import By
from framework.locator_constants import LocatorConstant, ElementNameConstant
from framework.tuple_utils import fill_locator_value
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BasicAuthForm(BaseForm):

    __page_name: str  = "Basic Auth"
    __success_msg_elemnt = PyQualityServices.element_factory.get_leble((By.XPATH,LocatorConstant.PRECISE_TEXT_LOCATOR.format("Congratulations! You must have the proper credentials"),"Successful Authentication"))

    def __init__(self):
        super(BasicAuthForm, self).__init__(
            (By.XPATH, LocatorConstant.PRECISE_TEXT_LOCATOR.format(self.__page_name)), self.__page_name)


    def is_success_msg_displayed(self):
        return self.__success_msg_elemnt.state.is_displayed