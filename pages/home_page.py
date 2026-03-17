class HomePage:
    def __init__(self, page):
        self.page = page
        self.from_port = "select[name='fromPort']"
        self.to_port = "select[name='toPort']"
        self.find_flights_btn = "input[type='submit']"

    def load(self):
        self.page.goto("https://blazedemo.com/index.php")

    def select_cities(self, from_city, to_city):
        self.page.select_option(self.from_port, label=from_city)
        self.page.select_option(self.to_port, label=to_city)

    def search_flights(self):
        self.page.click(self.find_flights_btn)