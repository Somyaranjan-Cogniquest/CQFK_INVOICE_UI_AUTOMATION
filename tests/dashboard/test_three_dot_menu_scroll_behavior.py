from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest


@pytest.mark.sanity
@pytest.mark.regression
def test_TC_80_three_dot_menu_persists_during_scroll(page):

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
    # FIND 100% DOCUMENT
    # ==========================
    rows = page.locator(
        "table tbody tr"
    )

    menu_opened = False

    for i in range(rows.count()):

        row = rows.nth(i)

        try:

            if "100%" in row.inner_text():

                print(
                    f"100% document found in row {i + 1}"
                )

                three_dot = row.locator(
                    "button.dropdown-toggle"
                )

                if three_dot.count() > 0:

                    three_dot.first.scroll_into_view_if_needed()

                    three_dot.first.click(
                        force=True
                    )

                    page.wait_for_timeout(2000)

                    menu_opened = True

                    break

        except Exception:
            continue

    assert menu_opened, \
        "Unable to open 3-dot menu"

    # ==========================
    # VERIFY MENU OPENED
    # ==========================
    menu_items = page.locator(
        "a.dropdown-item"
    )

    assert menu_items.count() > 0, \
        "Menu did not open"

    assert menu_items.first.is_visible(), \
        "Menu is not visible"

    print(
        "3-dot menu opened successfully"
    )

    # ==========================
    # SCROLL PAGE
    # ==========================
    page.mouse.wheel(
        0,
        1000
    )

    page.wait_for_timeout(3000)

    # ==========================
    # VERIFY MENU STILL OPEN
    # ==========================
    assert menu_items.first.is_visible(), \
        "Menu disappeared after scrolling"

    print(
        "PASS : Menu remained open "
        "and scrolled with the page"
    )