from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from test_data.test_data import USERNAME, PASSWORD
from config.config import LOGIN_URL, DASHBOARD_URL


def test_TC_01_valid_login(page):

    # Step 1: Open login page
    page.goto(LOGIN_URL)

    # Step 2: Login
    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    # Step 3: Wait for dashboard
    page.wait_for_url(DASHBOARD_URL)

    # Step 4: Dashboard check
    dashboard = DashboardPage(page)
    dashboard.is_loaded()