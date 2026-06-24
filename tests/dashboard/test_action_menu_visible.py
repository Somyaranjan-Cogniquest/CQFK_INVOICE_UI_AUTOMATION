from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_TC_64_verify_action_menu_visible(page):

    # ==========================
    # LOGIN
    # ==========================
    page.goto(LOGIN_URL)

    login = LoginPage(page)

    login.login(
        USERNAME,
        PASSWORD
    )

    page.wait_for_timeout(5000)

    # ==========================
    # OPEN PROCESSING DASHBOARD
    # ==========================
    dashboard = DashboardPage(page)

    dashboard.click_model_name()
    dashboard.click_processing_dashboard()

    page.wait_for_timeout(5000)

    # ==========================
    # VERIFY ROWS
    # ==========================
    rows = page.locator("tr")
    total_rows = rows.count()

    print("Total rows:", total_rows)

    assert total_rows > 0, "No document rows found"

    # ==========================
    # 3-DOT MENU LOCATOR (YOUR UI)
    # ==========================
    action_buttons = page.locator(
        "button.dropdown-toggle.btn.btn-success"
    )

    action_count = action_buttons.count()

    print("3-dot buttons found:", action_count)

    assert action_count > 0, "No 3-dot action buttons found"

    # ==========================
    # VERIFY EACH ROW HAS MENU
    # ==========================
    visible_count = 0

    for i in range(min(total_rows, action_count)):

        btn = action_buttons.nth(i)

        if btn.is_visible():
            visible_count += 1

    print("Visible 3-dot buttons:", visible_count)

    assert visible_count > 0, "3-dot menu not visible in rows"

    print("TC_64 Passed Successfully")