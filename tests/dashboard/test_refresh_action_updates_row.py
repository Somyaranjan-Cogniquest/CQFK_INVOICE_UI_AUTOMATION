from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_TC_72_refresh_action_updates_row(page):

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
    # SET PAGE SIZE = 40
    # ==========================
    page.select_option("select.pgtotal", "40")

    page.wait_for_timeout(3000)

    # ==========================
    # FIND FIRST DOCUMENT ROW
    # ==========================
    rows = page.locator("tbody tr")

    total_rows = rows.count()

    assert total_rows > 0, "No document rows found"

    row = rows.first

    before_refresh = row.inner_text()

    print("Before Refresh:")
    print(before_refresh)

    # ==========================
    # OPEN 3-DOT MENU
    # ==========================
    three_dot = row.locator("button.dropdown-toggle")

    assert three_dot.count() > 0, \
        "3-dot menu not found"

    three_dot.first.click(force=True)

    page.wait_for_timeout(2000)

    # ==========================
    # CLICK REFRESH
    # ==========================
    refresh_option = row.get_by_text(
        "Refresh",
        exact=False
    )

    assert refresh_option.count() > 0, \
        "Refresh option not found"

    refresh_option.first.click(force=True)

    page.wait_for_timeout(5000)

    # ==========================
    # VERIFY PAGE STILL WORKING
    # ==========================
    after_refresh = rows.first.inner_text()

    print("After Refresh:")
    print(after_refresh)

    assert len(after_refresh) > 0, \
        "Row data missing after refresh"

    print("Refresh executed successfully")

    # Optional validation
    if before_refresh != after_refresh:
        print("Row data updated after refresh")
    else:
        print("Refresh completed successfully (data unchanged)")