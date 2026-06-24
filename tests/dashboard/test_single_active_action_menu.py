from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_TC_67_single_row_action_menu(page):

    # ==========================
    # LOGIN
    # ==========================
    page.goto(LOGIN_URL)

    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    page.wait_for_timeout(5000)

    # ==========================
    # OPEN PROCESSING DASHBOARD
    # ==========================
    dashboard = DashboardPage(page)

    dashboard.click_model_name()
    dashboard.click_processing_dashboard()

    page.wait_for_timeout(5000)

    # ==========================
    # GET ALL 3-DOT MENUS
    # ==========================
    menus = page.locator("button.dropdown-toggle")

    total_menus = menus.count()

    assert total_menus >= 2, \
        "Less than 2 action menus found"

    # ==========================
    # OPEN ROW 1 MENU
    # ==========================
    first_menu = menus.nth(0)

    first_menu.scroll_into_view_if_needed()
    first_menu.click(force=True)

    page.wait_for_timeout(1500)

    first_dropdown = page.locator(".dropdown-menu.show").first

    assert first_dropdown.is_visible(), \
        "Row 1 menu did not open"

    print("Row 1 menu opened")

    # ==========================
    # OPEN ROW 2 MENU
    # ==========================
    second_menu = menus.nth(1)

    second_menu.scroll_into_view_if_needed()
    second_menu.click(force=True)

    page.wait_for_timeout(1500)

    visible_dropdowns = page.locator(".dropdown-menu.show")

    assert visible_dropdowns.count() == 1, \
        "More than one action menu is open"

    print("Only one menu remains open")

    assert visible_dropdowns.first.is_visible(), \
        "Row 2 menu not opened"

    print("TC_67 Passed Successfully")