import pytest

from framework.utils.spotify_client import SpotifyClient

@pytest.fixture(scope="session")
def api_client():
    return SpotifyClient()
