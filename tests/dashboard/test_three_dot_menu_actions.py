from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_TC_41_verify_three_dot_menu_actions(page):

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
    # FIND FIRST 100% DOCUMENT
    # ==========================
    rows = page.locator(
        "table tbody tr"
    )

    target_row = None

    for i in range(rows.count()):

        row = rows.nth(i)

        try:

            if "100%" in row.inner_text():

                target_row = row

                print(
                    f"100% Document Found : Row {i+1}"
                )

                break

        except Exception:

            continue

    assert target_row is not None, \
        "No 100% processed document found"

    # ==========================
    # OPEN 3-DOT MENU
    # ==========================
    three_dot = target_row.locator(
        "button.dropdown-toggle"
    )

    assert three_dot.count() > 0, \
        "Three-dot menu not found"

    three_dot.first.click(
        force=True
    )

    page.wait_for_timeout(3000)

    # ==========================
    # VERIFY MENU OPENED
    # ==========================
    menu_items = page.locator(
        "a.dropdown-item"
    )

    menu_count = menu_items.count()

    print(
        f"Menu Items Found : {menu_count}"
    )

    for i in range(menu_count):

        print(
            f"Menu {i+1} :",
            menu_items.nth(i).inner_text()
        )

    assert menu_count > 0, \
        "Action menu did not open"

    print(
        "Action menu opened successfully"
    )

    # ==========================
    # CLICK OUTSIDE MENU
    # ==========================
    page.mouse.click(
        10,
        10
    )

    page.wait_for_timeout(3000)

    # ==========================
    # VERIFY MENU CLOSED
    # ==========================
    assert (
        menu_items.count() == 0
        or
        not menu_items.first.is_visible()
    ), "Action menu did not close"

    print(
        "Action menu closed successfully"
    )

    print(
        "PASS : TC_41 Verify Three Dot Menu Actions"
    )