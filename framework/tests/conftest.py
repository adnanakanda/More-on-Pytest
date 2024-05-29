import pytest
from browser.py_quality_services import PyQualityServices
from core.utilities.json_settings_file import JsonSettingsFile
from framework.utils.browser_factory import BrowserFactory


def pytest_sessionstart(session):
    PyQualityServices.browser_factory = BrowserFactory()
    PyQualityServices.get_browser()

@pytest.fixture(scope="session", autouse = True)
def browser(request):
    settings = JsonSettingsFile("config.json")

    browser = PyQualityServices.get_browser()
    browser.maximize()
    browser.go_to(settings.get_value("url"))

    yield browser

    browser.quit()

@pytest.fixture(scope="session")
def base_url():
    settings = JsonSettingsFile("config.json")
    return settings.get_value("url")