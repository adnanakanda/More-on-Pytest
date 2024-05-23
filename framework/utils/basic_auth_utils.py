import base64
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v85.network import Headers

@pytest.mark.trio
async def basic_auth(prepare_browser_factory):
    driver = prepare_browser_factory.driver
    async with driver.bidi_connection() as connection:
        await connection.session.execute(connection.devtools.network.enable())

        credentials = base64.b64encode("admin:admin".encode()).decode()
        auth = {'authorization': 'Basic ' + credentials}

        await connection.session.execute(connection.devtools.network.set_extra_http_headers(Headers(auth)))

        return connection