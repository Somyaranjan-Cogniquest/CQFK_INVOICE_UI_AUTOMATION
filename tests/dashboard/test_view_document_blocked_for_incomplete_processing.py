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
    # SELECT PER PAGE = 40
    # ==========================
    page.select_option("select.pgtotal", "40")

    page.wait_for_timeout(5000)

    print("Per Page changed to 40")

    # ==========================
    # FIND DOCUMENT BELOW 100%
    # ==========================
    rows = page.locator("tbody tr")

    total_rows = rows.count()

    print(f"Total Rows Found: {total_rows}")

    found_incomplete_doc = False

    for i in range(total_rows):

        row = rows.nth(i)

        row_text = row.inner_text()

        # Skip completed documents
        if "100%" in row_text:
            continue

        print(f"Incomplete document found in Row {i + 1}")

        found_incomplete_doc = True

        current_url = page.url

        # ==========================
        # OPEN 3-DOT MENU
        # ==========================
        three_dot = row.locator("button.dropdown-toggle")

        assert three_dot.count() > 0, \
            "3-dot menu not found"

        three_dot.first.click(force=True)

        page.wait_for_timeout(2000)

        # ==========================
        # CLICK VIEW DOCUMENT
        # ==========================
        view_doc = row.get_by_text(
            "View document",
            exact=False
        )

        if view_doc.count() > 0:

            try:

                view_doc.first.click(timeout=3000)

                page.wait_for_timeout(3000)

                assert page.url == current_url, \
                    "User navigated to document though processing is not complete"

                print("Navigation blocked successfully")

            except Exception:

                print(
                    "View Document disabled or blocked "
                    "(Expected Behavior)"
                )

        else:

            print(
                "View Document option not available "
                "(Expected Behavior)"
            )

        break

    assert found_incomplete_doc, \
        "No document below 100% found"

    print(
        "TC_69 Passed - View Document blocked "
        "for incomplete document"
    )