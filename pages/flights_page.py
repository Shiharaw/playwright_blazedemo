class FlightsPage:
    def __init__(self, page):
        self.page = page
        self.flight_rows = "table tbody tr"
        self.choose_buttons = "input[type='submit']"

    def get_lowest_price_flight_index(self):
        rows = self.page.locator("table tbody tr")
        self.page.wait_for_selector("table tbody tr")

        prices = [
            float(rows.nth(i).locator("td").nth(5).inner_text().replace("$", "").strip())
            for i in range(rows.count())
        ]

        return prices.index(min(prices))

    def choose_flight(self, index):
        self.page.query_selector_all(self.choose_buttons)[index].click()