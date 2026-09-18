from playwright.sync_api import Page


class CheckoutCompletePage:
    """Page object for the SauceDemo Checkout Complete (confirmation) page."""

    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.title           = page.locator(".title")
        self.complete_header = page.locator("[data-test='complete-header']")
        self.complete_text   = page.locator("[data-test='complete-text']")
        self.back_home_button = page.locator("[data-test='back-to-products']")

