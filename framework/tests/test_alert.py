import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from browser.py_quality_services import PyQualityServices

from framework.forms.js_alert_from import JavaScriptAlertForm
from framework.forms.main_form import MainForm
from framework.tests.base_test import Test_base

class TestAlert(Test_base):
    __main_form: MainForm = MainForm()
    __js_alert_form: JavaScriptAlertForm = JavaScriptAlertForm()

    def test_alert(self):
       self.__main_form.get_navigation_link("JavaScript Alerts")
       self.__js_alert_form.click_js_alert_btn()
       assert self.__js_alert_form.is_success_message_displayed(), "Success message is not displayed"