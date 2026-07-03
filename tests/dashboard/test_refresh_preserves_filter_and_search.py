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
    # GET DOC ID FROM FIRST ROW
    # ==========================
    rows = page.locator("tbody tr")

    assert rows.count() > 0, \
        "No rows found"

    search_value = (
        rows.first
        .locator("td")
        .nth(1)
        .text_content()
        .strip()
    )

    print(f"Using Doc ID: {search_value}")

    # ==========================
    # SEARCH DOC ID
    # ==========================
    search_box = page.locator(
        "input.searchbar"
    )

    search_box.wait_for(
        state="visible"
    )

    search_box.fill(
        search_value
    )

    page.wait_for_timeout(1000)

    # ==========================
    # CLICK EXTEND SEARCH
    # ==========================
    extend_btn = page.locator(
        "button:has-text('Extend Search')"
    )

    if extend_btn.count() > 0:
        extend_btn.click()
        page.wait_for_timeout(5000)

    # ==========================
    # VERIFY SEARCH APPLIED
    # ==========================
    assert (
        search_box.input_value()
        == search_value
    ), "Search value not applied"

    rows = page.locator("tbody tr")

    total_rows = rows.count()

    print(
        f"Filtered Rows Found: {total_rows}"
    )

    assert total_rows > 0, \
        "No records found after search"

    # ==========================
    # OPEN ACTION MENU
    # ==========================
    first_row = rows.first

    three_dot = first_row.locator(
        "button.dropdown-toggle"
    )

    assert three_dot.count() > 0, \
        "3-dot menu not found"

    three_dot.first.click(
        force=True
    )

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

    refresh_option.click(
        force=True
    )

    page.wait_for_timeout(5000)

    print(
        "Refresh executed successfully"
    )

    # ==========================
    # VERIFY SEARCH PRESERVED
    # ==========================
    search_box = page.locator(
        "input.searchbar"
    )

    current_search = (
        search_box.input_value()
    )

    print(
        f"Search After Refresh: "
        f"{current_search}"
    )

    assert (
        current_search
        == search_value
    ), "Search value changed after refresh"

    # ==========================
    # VERIFY RESULTS STILL EXIST
    # ==========================
    rows_after = page.locator(
        "tbody tr"
    ).count()

    print(
        f"Rows After Refresh: "
        f"{rows_after}"
    )

    assert rows_after > 0, \
        "Filtered results disappeared"

    print(
        "TC_73 Passed - Refresh "
        "preserved search and filter state"
    )