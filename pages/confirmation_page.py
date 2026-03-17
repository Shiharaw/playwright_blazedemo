class ConfirmationPage:
    def __init__(self, page):
        self.page = page
        self.confirm_text = "h1"

    def get_confirmation_message(self):
        return self.page.inner_text(self.confirm_text)