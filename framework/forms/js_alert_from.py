from forms.base_form import BaseForm
from browser.py_quality_services import PyQualityServices
from selenium.webdriver.common.by import By
from framework.locator_constants import LocatorConstant, ElementNameConstant
from framework.tuple_utils import fill_locator_value

class JavaScriptAlertForm(BaseForm):
    __page_name = "JavaScript Alerts"
    __click_for_js_alert_btn = PyQualityServices.element_factory.get_button(By.XPATH("//button[@onclick='jsAlert()']"),"Click for JS Alert btn")
    __success_message_lbl = PyQualityServices.element_factory.get_label((By.XPATH, LocatorConstant.PRECISE_TEXT_LOCATOR.format("You successfully clicked an alert"), "Success message text"))


    def __init__(self):
        super(JavaScriptAlertForm, self).__init__((By.XPATH, LocatorConstant.PRECISE_TEXT_LOCATOR.format(self.__page_name)), self.__page_name)


    def click_js_alert_btn(self):
        self.__click_for_js_alert_btn.click()


    def is_success_message_displayed(self):
        return self.__success_message_lbl.is_displayed()
