import pytest
from framework.forms.wiki_main_form import Wiki_MainForm
from framework.forms.profile_form import ProfileForm
from framework.forms.file_download_form import FileDownloadForm


class Test_Wiki_UI:

    __to_be_searched = "Albert Einstein"
    wiki_main_form : Wiki_MainForm = Wiki_MainForm()
    profile_form : ProfileForm = ProfileForm()
    file_download_form : FileDownloadForm = FileDownloadForm()

    downloaded_PDF_name: str = file_download_form.get_pdf_name()

    def test_main_form(self):
        assert self.wiki_main_form.is_main_page_displayed("The Free Encyclopedia")," Main page is not displayed!"


    def test_search(self):
        self.wiki_main_form.search_text(self.__to_be_searched)
        self.wiki_main_form.click_search_btn()
        self.profile_form.click_tool_menu().click()
        self.profile_form.click_download_link().click()
        self.file_download_form.download_file().click()

        # assert if the file download is displayed or not
        assert self.file_download_form.is_file_download_link_displayed(self.downloaded_PDF_name),"File downloaded link is not displayed!"

