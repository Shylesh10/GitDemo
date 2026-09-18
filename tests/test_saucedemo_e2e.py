"""
End-to-End test for SauceDemo (https://www.saucedemo.com/)

Test data is loaded from: data/test_data.json

Scenario:
    1.  Open SauceDemo.
    2.  Log in with standard test credentials.
    3.  Verify the Products page is displayed.
    4.  Add a product to the cart.
    5.  Open the cart.
    6.  Verify the selected product is in the cart.
    7.  Proceed to checkout.
    8.  Enter checkout information.
    9.  Continue to the overview page.
    10. Verify the product and order summary on the overview page.
    11. Complete the purchase.
    12. Verify the successful order confirmation.
"""

import json
import pytest
from pathlib import Path
from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage

# ── Load test data from JSON ──────────────────────────────────────────────────
DATA_FILE = Path(__file__).parent.parent / "data" / "test_data.json"

with open(DATA_FILE, encoding="utf-8") as f:
    _data = json.load(f)

USERNAME     = _data["credentials"]["username"]
PASSWORD     = _data["credentials"]["password"]
PRODUCT_NAME = _data["product"]["name"]
FIRST_NAME   = _data["checkout"]["first_name"]
LAST_NAME    = _data["checkout"]["last_name"]
POSTAL_CODE  = _data["checkout"]["postal_code"]
# ─────────────────────────────────────────────────────────────────────────────


def test_saucedemo_e2e_purchase(
    login_page: LoginPage,
    inventory_page: InventoryPage,
    cart_page: CartPage,
    checkout_page: CheckoutPage,
    checkout_overview_page: CheckoutOverviewPage,
    checkout_complete_page: CheckoutCompletePage,
):
    """
    Single end-to-end test: Login → Add to cart → Checkout → Confirm order.
    All test data is driven from data/test_data.json.
    """

    # ── Step 1 & 2: Navigate and log in ──────────────────────────────────────
    login_page.navigate()
    login_page.login(USERNAME, PASSWORD)

    # ── Step 3: Verify Products page is displayed ─────────────────────────────
    expect(inventory_page.title).to_have_text("Products")

    # ── Step 4: Add product to the cart ──────────────────────────────────────
    inventory_page.add_product_to_cart(PRODUCT_NAME)
    # Verify cart badge shows 1 item
    expect(inventory_page.cart_badge).to_have_text("1")

    # ── Step 5: Open the cart ────────────────────────────────────────────────
    inventory_page.open_cart()

    # ── Step 6: Verify the cart page and the selected product ─────────────────
    expect(cart_page.title).to_have_text("Your Cart")
    expect(cart_page.get_cart_item(PRODUCT_NAME)).to_be_visible()

    # ── Step 7: Proceed to checkout ───────────────────────────────────────────
    cart_page.proceed_to_checkout()

    # ── Step 8: Enter checkout information ────────────────────────────────────
    expect(checkout_page.title).to_have_text("Checkout: Your Information")
    checkout_page.fill_information(FIRST_NAME, LAST_NAME, POSTAL_CODE)
    checkout_page.continue_to_overview()

    # ── Step 9 & 10: Verify overview page and order details ───────────────────
    expect(checkout_overview_page.title).to_have_text("Checkout: Overview")
    expect(checkout_overview_page.get_item_name(PRODUCT_NAME)).to_be_visible()
    expect(checkout_overview_page.summary_total).to_be_visible()

    # ── Step 11: Complete the purchase ───────────────────────────────────────
    checkout_overview_page.finish_order()

    # ── Step 12: Verify successful order confirmation ─────────────────────────
    expect(checkout_complete_page.title).to_have_text("Checkout: Complete!")
    expect(checkout_complete_page.complete_header).to_have_text(
        "Thank you for your order!"
    )
