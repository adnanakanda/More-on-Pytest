import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from browser.py_quality_services import PyQualityServices
from core.utilities.json_settings_file import JsonSettingsFile

from framework.forms.main_form import MainForm
from framework.utils.browser_factory import BrowserFactory


class Test_base:
    @pytest.fixture(scope="session", autouse=True)
    def prepare_browser_factory(request):
        settings = JsonSettingsFile("config.json")
        test_data = JsonSettingsFile("test_data.json")

        browser = PyQualityServices.get_browser()
        browser.maximize()
        browser.go_to(settings.get_value("url"))



        yield browser

        browser.quit()

