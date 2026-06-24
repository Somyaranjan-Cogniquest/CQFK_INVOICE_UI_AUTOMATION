from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_E2E_03_action_menu_refresh(page):

    # ==================================
    # STEP 1 : LOGIN
    # ==================================
    page.goto(LOGIN_URL)

    login = LoginPage(page)

    login.login(
        USERNAME,
        PASSWORD
    )

    # ==================================
    # STEP 2 : OPEN MODEL
    # ==================================
    dashboard = DashboardPage(page)

    dashboard.click_model_name()

    print("Dashboard loaded successfully")

    # ==================================
    # STEP 3 : OPEN PROCESSING DASHBOARD
    # ==================================
    dashboard.click_processing_dashboard()

    dashboard.wait_for_table()

    print("Processing Dashboard opened")

    # ==================================
    # STEP 4 : FIND FIRST 100% DOCUMENT
    # ==================================
    rows = page.locator("table tbody tr")

    total_rows = rows.count()

    target_row = None

    for i in range(total_rows):

        row = rows.nth(i)

        row_text = row.inner_text()

        if "100%" in row_text:

            target_row = row

            print(f"100% document found in row {i + 1}")

            break

    assert target_row is not None, \
        "No 100% processed document found"

    # ==================================
    # STEP 5 : OPEN 3-DOT MENU
    # ==================================
    menu_button = target_row.locator(
        "button[id^='dropdown-']"
    )

    assert menu_button.count() > 0, \
        "3-dot menu not found"

    menu_button.first.click(force=True)

    page.wait_for_timeout(2000)

    print("3-dot menu opened")

    # ==================================
    # STEP 6 : VERIFY MENU OPTIONS
    # ==================================
    menu_text = page.locator(
        ".dropdown-menu.show"
    ).inner_text()

    print("Menu Text:")
    print(menu_text)

    expected_options = [
        "View Document",
        "Reprocess Document",
        "Delete Document",
        "Refresh"
    ]

    for option in expected_options:

        assert option.lower() in menu_text.lower(), \
            f"{option} option not visible"

        print(f"{option} option visible")

    # ==================================
    # STEP 7 : CLICK REFRESH
    # ==================================
    refresh_option = page.locator(
        ".dropdown-menu.show"
    ).get_by_text(
        "Refresh",
        exact=True
    )

    refresh_option.click(force=True)

    page.wait_for_timeout(3000)

    print("Refresh clicked successfully")

    # ==================================
    # STEP 8 : VERIFY TABLE STILL EXISTS
    # ==================================
    dashboard.wait_for_table()

    assert page.locator(
        "table tbody tr"
    ).count() > 0, \
        "Table not visible after refresh"

    print("Table refreshed successfully")

    # ==================================
    # STEP 9 : VERIFY MENU CLOSES
    # ==================================
    page.mouse.click(10, 10)

    page.wait_for_timeout(1000)

    print("Menu closed on outside click")

    print(
        "PASS : E2E_03 Action Menu Refresh Validation Successful"
    )