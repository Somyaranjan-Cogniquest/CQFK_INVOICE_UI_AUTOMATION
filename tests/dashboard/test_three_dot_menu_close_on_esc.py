from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_TC_79_three_dot_menu_close_on_esc(page):

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

    menu_button = None

    for i in range(rows.count()):

        row = rows.nth(i)

        try:

            if "100%" in row.inner_text():

                btn = row.locator(
                    "button.dropdown-toggle"
                )

                if btn.count() > 0:

                    menu_button = btn.first

                    print(
                        f"100% Document Found : Row {i+1}"
                    )

                    break

        except Exception:

            continue

    assert menu_button is not None, \
        "No 100% processed document found"

    # ==========================
    # OPEN MENU
    # ==========================
    menu_button.click(
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

    assert menu_count > 0, \
        "3-dot menu did not open"

    print(
        "3-dot menu opened successfully"
    )

    # ==========================
    # PRESS ESC
    # ==========================
    page.keyboard.press(
        "Escape"
    )

    page.wait_for_timeout(3000)

    # ==========================
    # VERIFY MENU CLOSED
    # ==========================
    menu_closed = (
        menu_items.count() == 0
    )

    if not menu_closed:

        try:

            menu_closed = (
                not menu_items.first.is_visible()
            )

        except Exception:

            menu_closed = True

    assert menu_closed, \
        "3-dot menu did not close after ESC"

    print(
        "PASS : TC_79 Three Dot Menu Closed Successfully On ESC Key"
    )