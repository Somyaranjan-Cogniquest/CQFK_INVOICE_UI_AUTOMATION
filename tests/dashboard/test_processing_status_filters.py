from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_TC_34_processing_status_filters(page):

    # ==================================
    # LOGIN
    # ==================================
    page.goto(LOGIN_URL)

    login = LoginPage(page)

    login.login(
        USERNAME,
        PASSWORD
    )

    page.wait_for_timeout(5000)

    # ==================================
    # OPEN PROCESSING DASHBOARD
    # ==================================
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

        # ==================================
        # APPLY STATUS FILTER
        # ==================================
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

        # ==================================
        # FOR UNPROCESSED
        # APPLY FULL MONTH DATE RANGE
        # ==================================
        if (
            status == "Unprocessed"
            and row_count == 0
        ):

            print(
                "No Unprocessed documents found."
            )

            print(
                "Selecting full month date range..."
            )

            try:

                # Open calendar
                page.locator(
                    "img[src*='calendar']"
                ).first.click()

                page.wait_for_timeout(2000)

                # Select start date
                page.get_by_text(
                    "1",
                    exact=True
                ).first.click()

                page.wait_for_timeout(1000)

                # Select end date
                page.get_by_text(
                    "30",
                    exact=True
                ).first.click()

                page.wait_for_timeout(5000)

                rows = page.locator(
                    "table tbody tr"
                )

                row_count = rows.count()

                print(
                    "Rows After Date Filter = "
                    f"{row_count}"
                )

            except Exception as e:

                print(
                    "Unable to apply date filter:"
                )

                print(e)

        # ==================================
        # VALIDATION
        # ==================================
        assert row_count > 0, \
            f"No records found for {status}"

        print(
            f"{status} filter validated successfully"
        )

    print(
        "PASS : TC_34 Processing Status Filters"
    )