import os
import pytest
from browser.py_quality_services import PyQualityServices
from core.utilities.json_settings_file import JsonSettingsFile
from pathlib import Path

from selenium.webdriver.common.by import By

from framework.forms.wiki_main_form import Wiki_MainForm
from framework.forms.profile_form import ProfileForm
from framework.forms.file_download_form import FileDownloadForm
from framework.utils.file_utils import FileUtil


class Test_Wiki_UI:

    __to_be_searched = "Albert Einstein"
    wiki_main_form : Wiki_MainForm = Wiki_MainForm()
    profile_form : ProfileForm = ProfileForm()
    file_download_form : FileDownloadForm = FileDownloadForm()

    def test_main_form(self):
        assert self.wiki_main_form.is_main_page_displayed("The Free Encyclopedia")," Main page is not displayed!"


    def test_search(self):
        self.wiki_main_form.search_text(self.__to_be_searched)
        self.wiki_main_form.click_search_btn()
        self.profile_form.click_tool_menu()
        self.profile_form.click_download_link()
        self.file_download_form.download_file()
        self.__downloaded_PDF_name = self.file_download_form.get_pdf_name().text  #gets the file name.

        # assert if the file download is displayed or not
        assert self.file_download_form.is_file_download_link_displayed(self.__downloaded_PDF_name),"File downloaded link is not displayed!"
        filepath = FileUtil.get_target_file_path(self. __downloaded_PDF_name)
        print(f"File Path: {filepath}")

        file_address = f'file:{os.sep}{filepath}'
        print(f"File Address: {file_address}")
        label_file_content = PyQualityServices.element_factory.get_label((By.XPATH, '//pre'), 'text file content')

        assert PyQualityServices.conditional_wait.wait_for(lambda: FileUtil.is_file_downloaded(
            file_address, label_file_content), timeout=10) is True, 'File %s should be downloaded' % self.__downloaded_PDF_name