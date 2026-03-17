class PurchasePage:
    def __init__(self, page):
        self.page = page
        self.name = "#inputName"
        self.address = "#address"
        self.city = "#city"
        self.state = "#state"
        self.zip = "#zipCode"
        self.card = "#creditCardNumber"
        self.purchase_btn = "input[type='submit']"

    def fill_details(self):
        self.page.fill(self.name, "John Doe")
        self.page.fill(self.address, "123 Main Street")
        self.page.fill(self.city, "Colombo")
        self.page.fill(self.state, "Western")
        self.page.fill(self.zip, "10000")
        self.page.fill(self.card, "1234567890123456")

    def purchase(self):
        self.page.click(self.purchase_btn)