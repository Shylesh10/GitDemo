from playwright.sync_api import Page


class CheckoutOverviewPage:
    """Page object for the SauceDemo Checkout Step 2 (order overview)."""

    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.title         = page.locator(".title")
        self.finish_button = page.locator("[data-test='finish']")
        self.summary_total = page.locator("[data-test='total-label']")

    def get_item_name(self, product_name: str):
        """
        Return a locator for the overview item matching the given product name.
        Used for assertions in the test.
        """
        return self.page.locator(".cart_item").filter(has_text=product_name)

    def finish_order(self):
        """Click the Finish button to complete the purchase."""
        self.finish_button.click()

