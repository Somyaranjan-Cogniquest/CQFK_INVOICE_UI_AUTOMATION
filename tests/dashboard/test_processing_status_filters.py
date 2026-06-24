from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.smoke
@pytest.mark.regression
def test_TC_34_processing_status_filters(page):

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

    statuses = [
        "Processed",
        "Unprocessed"
    ]

    for status in statuses:

        print(f"\nValidating {status}")

        dashboard.open_doc_status_dropdown()

        dashboard.select_doc_status(status)

        page.wait_for_timeout(5000)

        rows = page.locator(
            "table tbody tr"
        )

        row_count = rows.count()

        print(
            f"Rows Found = {row_count}"
        )

        assert row_count > 0, \
            f"No records found for {status}"

        print(
            f"{status} filter validated successfully"
        )

    print(
        "PASS : TC_34 Processing Status Filters"
    )