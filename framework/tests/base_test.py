import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from browser.py_quality_services import PyQualityServices
from core.utilities.json_settings_file import JsonSettingsFile
from framework.forms.main_form import MainForm


class Test_base:

    @pytest.fixture(autouse = True)
    def setup(self):
        self.settings = JsonSettingsFile("config.json")
        #self.test_data = JsonSettingsFile("test_data.json")

        self.browser = PyQualityServices.get_browser()
        self.browser.maximize()
        self.browser.go_to(self.settings.get_value("url"))

        yield

        self.browser.quit()

