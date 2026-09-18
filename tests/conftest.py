import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage


# ---------------------------------------------------------------------------
# Page Object Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    """Provide a LoginPage instance backed by the active Playwright page."""
    return LoginPage(page)


@pytest.fixture
def inventory_page(page: Page) -> InventoryPage:
    """Provide an InventoryPage instance backed by the active Playwright page."""
    return InventoryPage(page)


@pytest.fixture
def cart_page(page: Page) -> CartPage:
    """Provide a CartPage instance backed by the active Playwright page."""
    return CartPage(page)


@pytest.fixture
def checkout_page(page: Page) -> CheckoutPage:
    """Provide a CheckoutPage instance backed by the active Playwright page."""
    return CheckoutPage(page)


@pytest.fixture
def checkout_overview_page(page: Page) -> CheckoutOverviewPage:
    """Provide a CheckoutOverviewPage instance backed by the active Playwright page."""
    return CheckoutOverviewPage(page)


@pytest.fixture
def checkout_complete_page(page: Page) -> CheckoutCompletePage:
    """Provide a CheckoutCompletePage instance backed by the active Playwright page."""
    return CheckoutCompletePage(page)

