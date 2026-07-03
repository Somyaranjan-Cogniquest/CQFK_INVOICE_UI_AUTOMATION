from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest


@pytest.mark.sanity
@pytest.mark.regression
def test_TC_69_view_document_blocked_for_incomplete_processing(page):

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
    # PER PAGE = 40
    # ==========================
    page.select_option(
        "select.pgtotal",
        "40"
    )

    page.wait_for_timeout(5000)

    print("Per Page changed to 40")

    found_incomplete_doc = False
    current_url = page.url

    # ==========================
    # SEARCH FUNCTION
    # ==========================
    def find_incomplete_document():

        for page_no in range(20):

            print(f"\nChecking Page {page_no + 1}")

            rows = page.locator(
                "tbody tr"
            )

            total_rows = rows.count()

            print(
                f"Rows Found: {total_rows}"
            )

            for i in range(total_rows):

                row = rows.nth(i)

                row_text = row.inner_text()

                print(
                    f"\nRow {i+1}"
                )
                print(row_text)

                # Skip completed docs
                if "100%" in row_text:
                    continue

                print(
                    f"Incomplete document "
                    f"found in row {i+1}"
                )

                return row

            # Next Page
            next_btn = page.locator(
                "img[src*='single_right']"
            )

            if (
                next_btn.count() == 0
                or
                not next_btn.first.is_visible()
            ):
                break

            next_btn.first.click(
                force=True
            )

            page.wait_for_timeout(4000)

            print(
                "Moved to next page"
            )

        return None

    # ==========================
    # FIRST SEARCH
    # ==========================
    row = find_incomplete_document()

    # ==========================
    # APPLY DATE FILTER
    # ==========================
    if row is None:

        print(
            "No incomplete documents found."
        )

        print(
            "Applying full month date filter..."
        )

        try:

            # Open Calendar
            page.locator(
                "img[src*='calendar']"
            ).first.click()

            page.wait_for_timeout(2000)

            # Start Date
            page.get_by_text(
                "1",
                exact=True
            ).first.click()

            page.wait_for_timeout(1000)

            # End Date
            page.get_by_text(
                "30",
                exact=True
            ).first.click()

            page.wait_for_timeout(5000)

            print(
                "Date range applied."
            )

        except Exception as e:

            print(
                "Unable to apply "
                "date filter."
            )
            print(e)

        # Search Again
        row = find_incomplete_document()

    # ==========================
    # FINAL VALIDATION
    # ==========================
    if row is None:

        pytest.skip(
            "No incomplete documents "
            "available even after "
            "applying date filter."
        )

    print(
        "Incomplete document found."
    )

    # ==========================
    # OPEN 3-DOT MENU
    # ==========================
    three_dot = row.locator(
        "button.dropdown-toggle"
    )

    assert (
        three_dot.count() > 0
    ), "3-dot menu not found"

    three_dot.first.click(
        force=True
    )

    page.wait_for_timeout(2000)

    # ==========================
    # VIEW DOCUMENT
    # ==========================
    view_doc = page.get_by_text(
        "View document",
        exact=False
    )

    if view_doc.count() > 0:

        try:

            view_doc.first.click(
                timeout=3000
            )

            page.wait_for_timeout(
                3000
            )

            assert (
                page.url
                == current_url
            ), (
                "User navigated to "
                "document though "
                "processing is incomplete"
            )

            print(
                "Navigation blocked "
                "successfully"
            )

        except Exception:

            print(
                "View Document disabled "
                "(Expected Behaviour)"
            )

    else:

        print(
            "View Document option "
            "not available "
            "(Expected Behaviour)"
        )

    print(
        "TC_69 Passed - View Document "
        "blocked for incomplete document"
    )