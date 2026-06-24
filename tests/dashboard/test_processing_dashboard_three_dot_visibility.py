from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_TC_64_verify_action_menu(page):

    # =========================
    # LOGIN
    # =========================
    page.goto(LOGIN_URL)

    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    page.wait_for_timeout(5000)

    # =========================
    # NAVIGATE
    # =========================
    dashboard = DashboardPage(page)
    dashboard.click_model_name()
    dashboard.click_processing_dashboard()

    page.wait_for_timeout(5000)

    # =========================
    # FIND 100% ROW
    # =========================
    rows = page.locator("tr")
    count = rows.count()

    target_row = None

    for i in range(count):
        row = rows.nth(i)
        if "100%" in row.inner_text():
            target_row = row
            break

    assert target_row is not None, "No 100% processed document found"

    # =========================
    # CLICK 3-DOT INSIDE THAT ROW
    # =========================
    three_dot = target_row.locator("button.dropdown-toggle")
    three_dot.wait_for(state="visible", timeout=10000)
    three_dot.click()

    page.wait_for_timeout(1500)

    # =========================
    # VERIFY MENU OPTIONS (SCOPED FIX)
    # =========================
    menu = target_row.locator(".dropdown-menu")

    expected_options = [
        "View Document",
        "Reprocess Document",
        "Delete Document",
        "Refresh"
    ]

    for option in expected_options:
        assert menu.get_by_text(option).is_visible(), f"{option} not visible"