from playwright.sync_api import Page, expect
import os

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def handle_dialog(self, trigger_action, expected_text=None, accept=True, input_text=None, dialog_expected=True):
        def on_dialog(dialog):
            if dialog_expected == True:

                ## kontrola ocakavneho textu (ak je nejaky)
                if expected_text and expected_text not in dialog.message:
                    raise AssertionError(f"Unexpected dialog message: {dialog.message}")

                ## akceptuj alebo odmietni (ak je tam text field a je k dispozici input text vlozi ho)
                if accept:
                    dialog.accept(input_text)

                else:
                    dialog.dismiss()
            ## volam funkciu definovanú vyššie
            self.page.once("dialog", on_dialog)

            ## spuštam labda trigger funkciu
            trigger_action()

    def upload_file(self,trigger_action, filepath):
        def on_fc(fc):
            fc.set_files(filepath)

        self.page.once("filechooser", on_fc)

        trigger_action()

    def get_title(self):
        return self.page.title()

    def download_file(self, trigger_action):
        with self.page.expect_download() as download_info:
            trigger_action()

        download = download_info.value

        assert download.suggested_filename.endswith(".txt")

        download.save_as("downloads/invoice.txt")
        assert os.path.exists("downloads/invoice.txt")








