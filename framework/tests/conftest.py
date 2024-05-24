import pytest
from browser.py_quality_services import PyQualityServices
from core.utilities.json_settings_file import JsonSettingsFile

from framework.utils.browser_factory import BrowserFactory


def pytest_sessionstart(session):
    PyQualityServices.browser_factory = BrowserFactory()
    PyQualityServices.get_browser()

@pytest.fixture(scope="session")
def browser(request):
    settings = JsonSettingsFile("config.json")
    test_data = JsonSettingsFile("test_data.json")

    browser = PyQualityServices.get_browser()
    browser.maximize()
    browser.go_to(settings.get_value("url"))

    yield browser

    browser.quit()