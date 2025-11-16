from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def handle_dialog(self, trigger_action, expected_text=None, accept=True, input_text=None):
        def on_dialog(dialog):
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







