import base64
import pytest
from browser.py_quality_services import PyQualityServices
from framework.forms.basic_auth_form import BasicAuthForm
from selenium.webdriver.common.devtools.v85.network import Headers

class TestBasicAuth():

    @pytest.mark.trio
    async def test_basic_auth(self, browser):
        __basic_auth_form: BasicAuthForm = BasicAuthForm()
        async with browser.driver.bidi_connection() as connection:
            await connection.session.execute(connection.devtools.network.enable())

            credentials = base64.b64encode("admin:admin".encode()).decode()
            auth = {'Authorization': 'Basic ' + credentials}

            await connection.session.execute(connection.devtools.network.set_extra_http_headers(Headers(auth)))

            browser.go_to('https://the-internet.herokuapp.com/basic_auth')

        assert __basic_auth_form.is_success_msg_displayed(), "Success message is not displayed!"

