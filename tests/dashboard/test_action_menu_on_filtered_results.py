from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_TC_75_action_menu_on_filtered_results(page):

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
    # APPLY SEARCH AS FILTER
    # ==========================
    search_box = page.locator("input.searchbar")

    search_box.wait_for(state="visible")

    search_box.fill("71460")

    page.wait_for_timeout(3000)

    rows = page.locator("tbody tr")

    filtered_count = rows.count()

    print(f"Filtered Rows: {filtered_count}")

    assert filtered_count > 0, \
        "No filtered records found"

    # ==========================
    # OPEN 3-DOT MENU
    # ==========================
    first_row = rows.first

    three_dot = first_row.locator(
        "button.dropdown-toggle"
    )

    assert three_dot.count() > 0, \
        "3-dot menu not found"

    three_dot.first.click(force=True)

    page.wait_for_timeout(2000)

    # ==========================
    # VERIFY MENU OPTIONS
    # ==========================
    refresh_option = page.get_by_text(
        "Refresh",
        exact=False
    ).first

    assert refresh_option.is_visible(), \
        "Refresh option not visible"

    # ==========================
    # CLICK REFRESH
    # ==========================
    refresh_option.click(force=True)

    page.wait_for_timeout(5000)

    # ==========================
    # VERIFY FILTER STILL EXISTS
    # ==========================
    current_search = search_box.input_value()

    assert current_search == "71460", \
        "Filter/Search lost after action"

    rows_after = page.locator("tbody tr").count()

    assert rows_after > 0, \
        "Filtered rows disappeared"

    print(
        "TC_75 Passed - Action menu works "
        "on filtered results"
    )