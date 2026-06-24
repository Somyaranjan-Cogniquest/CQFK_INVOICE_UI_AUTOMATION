from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_TC_80_three_dot_menu_scroll_behavior(page):

    page.goto(LOGIN_URL)

    login = LoginPage(page)

    login.login(
        USERNAME,
        PASSWORD
    )

    page.wait_for_timeout(5000)

    dashboard = DashboardPage(page)

    dashboard.click_model_name()

    dashboard.click_processing_dashboard()

    page.wait_for_timeout(5000)

    rows = page.locator(
        "table tbody tr"
    )

    menu_opened = False

    for i in range(rows.count()):

        row = rows.nth(i)

        try:

            if "100%" in row.inner_text():

                three_dot = row.locator(
                    "button.dropdown-toggle"
                )

                if three_dot.count() > 0:

                    three_dot.first.click(
                        force=True
                    )

                    page.wait_for_timeout(2000)

                    menu_opened = True

                    break

        except Exception:

            continue

    assert menu_opened, \
        "Unable to open menu"

    menu_items = page.locator(
        "a.dropdown-item"
    )

    assert menu_items.count() > 0, \
        "Menu did not open"

    print("Menu opened successfully")

    # Scroll page
    page.mouse.wheel(
        0,
        1000
    )

    page.wait_for_timeout(3000)

    # Verify menu closed
    menu_closed = False

    try:

        menu_closed = (
            not menu_items.first.is_visible()
        )

    except Exception:

        menu_closed = True

    assert menu_closed, \
        "Menu remained visible after scroll"

    print(
        "PASS : Menu closed automatically after scrolling"
    )