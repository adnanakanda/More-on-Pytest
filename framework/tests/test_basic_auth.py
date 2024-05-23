import pytest
from framework.forms.main_form import MainForm
from framework.tests.base_test import Test_base
from framework.forms.basic_auth_form import BasicAuthForm
from framework.utils.basic_auth_utils import basic_auth
class TestBasicAuth(Test_base):

    __main_form: MainForm = MainForm()
    __basic_auth_form: BasicAuthForm = BasicAuthForm()

    @pytest.mark.trio
    async def test_basic_auth_wrapper(self, prepare_browser_factory):
        browser = prepare_browser_factory
        await basic_auth(browser)
        self.__main_form.get_navigation_link("Basic Auth").click()
        assert self.__basic_auth_form.is_success_msg_displayed(), "Success message is not displayed!"


        """try:
            assert self.__basic_auth_form.is_success_msg_displayed(), "Success message is not displayed!"
        except AssertionError as e:
            # Log the error or take other appropriate actions
            # For example:
            print(f"AssertionError: {e}")
            # You can re-raise the exception if you want the test to fail
            raise"""

