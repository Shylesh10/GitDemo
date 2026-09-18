from playwright.sync_api import Page


class CartPage:
    """Page object for the SauceDemo Cart page."""

    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.title           = page.locator(".title")
        self.checkout_button = page.locator("[data-test='checkout']")

    def get_cart_item(self, product_name: str):
        """
        Return a locator for a cart item containing the given product name.
        Used for assertions in the test.
        """
        return self.page.locator(".cart_item").filter(has_text=product_name)

    def proceed_to_checkout(self):
        """Click the Checkout button."""
        self.checkout_button.click()

