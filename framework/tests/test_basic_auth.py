import pytest
from framework.forms.main_form import MainForm
from framework.tests.base_test import Test_base
from framework.forms.basic_auth_form import BasicAuthForm
class TestBasicAuth(Test_base):

    __main_form: MainForm = MainForm()
    __basic_auth_form: BasicAuthForm = BasicAuthForm()



    """def basic_authorisation(self, prepare_browser_factory):
        browser = prepare_browser_factory
        """

    def test_basic_auth(self, prepare_browser_factory):
        browser = prepare_browser_factory
        self.__main_form.get_navigation_link("Basic Auth").click()
        assert self.__basic_auth_form.is_success_msg_displayed(), "Success message is not displayed!"

