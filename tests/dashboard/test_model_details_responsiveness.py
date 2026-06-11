from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def test_TC_31_model_details_responsiveness(page):

    # Open login page
    page.goto(LOGIN_URL)

    # Login
    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    page.wait_for_timeout(3000)

    # Dashboard
    dashboard = DashboardPage(page)

    # Open model landing page
    dashboard.click_model_name()

    page.wait_for_timeout(3000)

    # =========================
    # RESPONSIVENESS CHECKS
    # =========================

    # Small screen (mobile)
    page.set_viewport_size({"width": 375, "height": 667})
    page.wait_for_timeout(2000)

    assert dashboard.is_home_visible()

    # Medium screen (tablet)
    page.set_viewport_size({"width": 768, "height": 1024})
    page.wait_for_timeout(2000)

    assert dashboard.is_home_visible()

    # Large screen (desktop)
    page.set_viewport_size({"width": 1366, "height": 768})
    page.wait_for_timeout(2000)

    assert dashboard.is_home_visible()