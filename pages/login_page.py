from playwright.sync_api import Page


class LoginPage:
    """Page object for the SauceDemo login page."""

    URL = "https://www.saucedemo.com/"

    def __init__(self, page: Page):
        self.page = page

        # Locators using Playwright's recommended data-test attributes
        self.username_input = page.locator("[data-test='username']")
        self.password_input = page.locator("[data-test='password']")
        self.login_button   = page.locator("[data-test='login-button']")

    def navigate(self):
        """Navigate to the SauceDemo login page."""
        self.page.goto(self.URL)

    def login(self, username: str, password: str):
        """Fill in credentials and submit the login form."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

