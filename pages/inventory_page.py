from playwright.sync_api import Page


class InventoryPage:
    """Page object for the SauceDemo Products (inventory) page."""

    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.title      = page.locator(".title")
        self.cart_link  = page.locator("[data-test='shopping-cart-link']")
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")

    def add_product_to_cart(self, product_name: str):
        """
        Click the 'Add to cart' button for a specific product by its name.
        Uses a relative locator: find the product card containing the name,
        then click its button within that card.
        """
        # Locate the inventory item that contains the given product name
        product_card = self.page.locator(".inventory_item").filter(
            has_text=product_name
        )
        product_card.locator("button").click()

    def open_cart(self):
        """Click the cart icon to open the shopping cart page."""
        self.cart_link.click()

