import pytest

from browser.py_quality_services import PyQualityServices
from core.utilities.json_settings_file import JsonSettingsFile
from framework.utils.browser_factory import BrowserFactory
from framework.utils.spotify_client import SpotifyClient

@pytest.fixture(scope="session")
def api_client():
    return SpotifyClient()