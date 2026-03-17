from playwright.sync_api import sync_playwright

from playwright_blazedemo.pages.confirmation_page import ConfirmationPage
from playwright_blazedemo.pages.flights_page import FlightsPage
from playwright_blazedemo.pages.home_page import HomePage
from playwright_blazedemo.pages.purchase_page import PurchasePage


def test_booking_flow():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Home Page
        home = HomePage(page)
        home.load()
        home.select_cities("Boston", "London")
        home.search_flights()

        # Flights Page
        flights = FlightsPage(page)
        index = flights.get_lowest_price_flight_index()
        flights.choose_flight(index)

        # Purchase Page
        purchase = PurchasePage(page)
        purchase.fill_details()
        purchase.purchase()

        # Confirmation Page
        confirm = ConfirmationPage(page)
        message = confirm.get_confirmation_message()

        assert "Thank you" in message

        browser.close()