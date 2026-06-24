from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_TC_73_refresh_preserves_filter_and_search(page):

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
    # APPLY SEARCH
    # ==========================
    search_value = "71460"

    search_box = page.locator("input.searchbar")

    search_box.wait_for(state="visible")

    search_box.fill(search_value)

    page.wait_for_timeout(3000)

    assert search_box.input_value() == search_value, \
        "Search value not applied"

    print(f"Search Applied: {search_value}")

    # ==========================
    # VERIFY FILTERED DATA EXISTS
    # ==========================
    rows = page.locator("tbody tr")

    total_rows = rows.count()

    assert total_rows > 0, \
        "No records found after search"

    print(f"Filtered Rows Found: {total_rows}")

    # ==========================
    # OPEN FIRST ROW 3-DOT MENU
    # ==========================
    first_row = rows.first

    three_dot = first_row.locator("button.dropdown-toggle")

    assert three_dot.count() > 0, \
        "3-dot menu not found"

    three_dot.first.click(force=True)

    page.wait_for_timeout(2000)

    # ==========================
    # CLICK REFRESH
    # ==========================
    refresh_option = page.get_by_text(
        "Refresh",
        exact=False
    ).first

    assert refresh_option.is_visible(), \
        "Refresh option not visible"

    refresh_option.click(force=True)

    page.wait_for_timeout(5000)

    print("Refresh executed successfully")

    # ==========================
    # RE-LOCATE SEARCH BOX
    # ==========================
    search_box = page.locator("input.searchbar")

    search_box.wait_for(state="visible")

    # ==========================
    # VERIFY SEARCH VALUE PRESERVED
    # ==========================
    current_search = search_box.input_value()

    print(f"Search After Refresh: {current_search}")

    assert current_search == search_value, \
        "Search value changed after refresh"

    # ==========================
    # VERIFY FILTERED RESULTS REMAIN
    # ==========================
    rows = page.locator("tbody tr")

    row_count_after_refresh = rows.count()

    assert row_count_after_refresh > 0, \
        "Filtered results disappeared after refresh"

    print(
        f"Rows After Refresh: "
        f"{row_count_after_refresh}"
    )

    print(
        "TC_73 Passed - Refresh preserved "
        "search and filter state"
    )