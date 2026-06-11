from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD


def test_TC_12_verify_model_names_are_clickable(page):

    # Login
    page.goto(LOGIN_URL)

    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    page.wait_for_url("**/dashboard")

    # Click model name
    dashboard = DashboardPage(page)
    dashboard.click_model_name()

    # Wait for next page
    page.wait_for_load_state("networkidle")

    # Verify navigation
    assert page.url != "https://cqfk-invoice.cogniquest.ai/InvIDPApi/dashboard"

    print("Model Landing page opened successfully")