from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_TC_38C_year_navigation(page):

    page.goto(LOGIN_URL)

    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    page.wait_for_timeout(5000)

    dashboard = DashboardPage(page)

    dashboard.click_model_name()
    dashboard.click_processing_dashboard()

    page.wait_for_timeout(3000)

    # Open calendar
    page.locator("img.datepick").click()

    page.wait_for_timeout(2000)

    # Open year picker
    page.get_by_text("2026").first.click()

    page.wait_for_timeout(2000)

    # Verify year list opened
    assert page.get_by_text("2025").is_visible()

    # Select previous year
    page.get_by_text("2025").click()

    page.wait_for_timeout(2000)

    # Verify selected year displayed
    assert page.get_by_text("2025").first.is_visible()