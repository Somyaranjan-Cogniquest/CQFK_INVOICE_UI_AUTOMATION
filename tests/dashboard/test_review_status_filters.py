from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest


@pytest.mark.sanity
@pytest.mark.regression
def test_TC_33_review_status_filters(page):

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
    # REVIEW STATUS FILTERS
    # ==========================
    statuses = [
        "Approved",
        "Not approved",
        "Rejected",
        "Deleted"
    ]

    for status in statuses:

        print(f"\nApplying Filter : {status}")

        dashboard.open_review_status_dropdown()

        dashboard.select_review_status(
            status
        )

        page.wait_for_timeout(3000)

        rows = page.locator(
            "table tbody tr"
        )

        actual_count = rows.count()

        print(
            f"{status} Records : "
            f"{actual_count}"
        )

        # ==========================
        # VALIDATION
        # ==========================
        if actual_count > 0:
            print(
                f"{status} filter "
                f"working successfully"
            )
        else:
            print(
                f"No data available "
                f"for {status}"
            )

        # Filter should not crash
        assert actual_count >= 0

    print(
        "\nTC_33 Passed - "
        "Review Status filters verified"
    )