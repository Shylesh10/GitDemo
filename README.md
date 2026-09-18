# SauceDemo Playwright Automation Framework

A beginner-friendly end-to-end automated test for [SauceDemo](https://www.saucedemo.com/) built with **Python**, **Playwright**, **pytest**, and the **Page Object Model (POM)**.
A beginner-friendly end-to-end automated test for [SauceDemo](https://www.saucedemo.com/) built with **Python**, **Playwright**, **pytest**, and the **Page Object Model (POM)**. Supports **Jenkins** and **GitHub Actions** CI/CD pipelines.

---

## Project Structure

```
saucedemo_playwright/
│
├── .github/
│   └── workflows/
│       └── playwright.yml         # GitHub Actions CI/CD pipeline
│
├── data/
│   └── test_data.json             # All test data (credentials, product, checkout info)
│
├── pages/
│   ├── __init__.py
│   ├── login_page.py              # Login page interactions
│   ├── inventory_page.py          # Products page interactions
│   ├── cart_page.py               # Shopping cart interactions
│   ├── checkout_page.py           # Checkout Step 1: Customer info
│   ├── checkout_overview_page.py  # Checkout Step 2: Order overview
│   └── checkout_complete_page.py  # Checkout Step 3: Confirmation
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py                # Pytest fixtures (page objects)
│   └── test_saucedemo_e2e.py      # The single E2E test
│   └── test_saucedemo_e2e.py      # The single E2E test (reads data from JSON)
│
├── reports/                       # Auto-generated HTML reports
│   └── report.html
│
├── Jenkinsfile                    # Jenkins declarative pipeline
├── pytest.ini                     # Pytest settings (headed mode + HTML report)
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

---

## Test Data

All test data lives in [`data/test_data.json`](data/test_data.json). You can change credentials, product, or checkout info without touching any test code:

```json
{
  "credentials": {
    "username": "standard_user",
    "password": "secret_sauce"
  },
  "product": {
    "name": "Sauce Labs Backpack"
  },
  "checkout": {
    "first_name": "John",
    "last_name": "Doe",
    "postal_code": "12345"
  }
}
```

---

## Prerequisites

- Python 3.9+
- Google Chrome browser installed
- Google Chrome browser installed (for local headed runs)

---

## Setup
## Local Setup

### 1. Install Python dependencies

```powershell
pip install -r requirements.txt
```

### 2. Install Playwright browsers (only needed once)

```powershell
playwright install
```

---

## Running the Test
## Running the Test Locally

From the `saucedemo_playwright/` folder, run:
From the `saucedemo_playwright/` folder:

```powershell
pytest
# Headed (visible browser) with slow-motion — recommended while learning
python -m pytest tests/test_saucedemo_e2e.py -v --headed --slowmo=800 --html=reports/report.html --self-contained-html

# Headless (no browser window) — faster
python -m pytest tests/test_saucedemo_e2e.py -v --headless --html=reports/report.html --self-contained-html
```

This will automatically:
- Launch Chrome in **headed (visible)** mode
- Run the full end-to-end test
- Generate an **HTML report** at `reports/report.html`
### View the HTML Report

```powershell
start reports\report.html
```

---

## Viewing the HTML Report
## CI/CD

After the test completes, open the report in your browser:
### GitHub Actions

```powershell
start reports\report.html
```
The workflow is in [`.github/workflows/playwright.yml`](.github/workflows/playwright.yml).

It triggers automatically on:
- Every **push** to `main` or `master`
- Every **pull request** to `main` or `master`

Steps it runs:
1. Checkout code
2. Set up Python 3.11
3. Install dependencies
4. Install Playwright Chromium browser
5. Run tests in **headless mode**
6. Upload `reports/report.html` as a downloadable artifact (kept for 14 days)

**To view the report** after a GitHub Actions run:
> Go to the Actions tab → click the workflow run → scroll to **Artifacts** → download `playwright-report`.

---

### Jenkins

The [`Jenkinsfile`](Jenkinsfile) defines a declarative pipeline with these stages:

| Stage | What it does |
|-------|-------------|
| Checkout | Pulls latest code from GitHub |
| Install Dependencies | `pip install -r requirements.txt` |
| Install Playwright Browsers | `playwright install chromium --with-deps` |
| Run Tests | Runs tests in headless mode |

**Post-build:**
- Archives `reports/report.html` as a build artifact
- Publishes the report in the Jenkins job sidebar via the **HTML Publisher plugin**

#### Jenkins Setup Requirements
- **HTML Publisher Plugin** installed in Jenkins
- Jenkins agent has **Python 3.9+** installed
- Jenkins agent has internet access to install pip packages

#### Jenkins Pipeline Setup
1. Create a new **Pipeline** job in Jenkins
2. Set **Definition** to `Pipeline script from SCM`
3. Set **SCM** to `Git` and provide your repository URL
4. Set **Script Path** to `saucedemo_playwright/Jenkinsfile`
5. Save and click **Build Now**

---

## Test Scenario

The single E2E test covers:

| Step | Action |
|------|--------|
| 1 | Open SauceDemo (https://www.saucedemo.com/) |
| 2 | Log in with `standard_user` / `secret_sauce` |
| 2 | Log in with credentials from `data/test_data.json` |
| 3 | Verify Products page is displayed |
| 4 | Add "Sauce Labs Backpack" to cart |
| 4 | Add product from `data/test_data.json` to cart |
| 5 | Open the cart |
| 6 | Verify the product is in the cart |
| 7 | Proceed to checkout |
| 8 | Enter customer info (John Doe, 12345) |
| 8 | Enter customer info from `data/test_data.json` |
| 9 | Continue to order overview |
| 10 | Verify product and summary on overview |
| 11 | Complete the purchase |
| 12 | Verify "Thank you for your order!" confirmation |

---

## Running in Headless Mode (no browser window)
## Upload to GitHub

```powershell
pytest --headless
# From the saucedemo_playwright/ folder
git init
git add .
git commit -m "Initial commit: SauceDemo Playwright E2E framework"
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```

---

## Credentials Used

| Field | Value |
|-------|-------|
| Username | `standard_user` |
| Password | `secret_sauce` |

Once pushed, GitHub Actions will automatically pick up `.github/workflows/playwright.yml` and run on every push!
