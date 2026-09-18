from playwright.sync_api import Page


class CheckoutPage:
    """Page object for the SauceDemo Checkout Step 1 (information entry)."""

    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.title            = page.locator(".title")
        self.first_name_input = page.locator("[data-test='firstName']")
        self.last_name_input  = page.locator("[data-test='lastName']")
        self.postal_code_input = page.locator("[data-test='postalCode']")
        self.continue_button  = page.locator("[data-test='continue']")

    def fill_information(self, first_name: str, last_name: str, postal_code: str):
        """Enter customer information into the checkout form."""
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)

    def continue_to_overview(self):
        """Click the Continue button to proceed to the order overview."""
        self.continue_button.click()

