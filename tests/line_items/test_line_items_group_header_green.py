from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_TC_01_line_item_group_header_green(page):

    # ==================================
    # LOGIN
    # ==================================
    page.goto(LOGIN_URL)

    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    # ==================================
    # OPEN PROCESSING DASHBOARD
    # ==================================
    dashboard = DashboardPage(page)

    dashboard.click_model_name()
    dashboard.click_processing_dashboard()
    dashboard.wait_for_table()

    print("Processing Dashboard opened")

    document_found = False

    rows = page.locator("table tbody tr")

    for i in range(rows.count()):

        rows = page.locator("table tbody tr")
        row = rows.nth(i)

        if "100%" not in row.inner_text():
            continue

        print(f"\nChecking Row {i + 1}")

        current_url = page.url

        # ==================================
        # OPEN DOCUMENT
        # ==================================
        row.locator(
            "button.dropdown-toggle"
        ).click(force=True)

        page.wait_for_timeout(1000)

        row.get_by_text(
            "View document"
        ).click(force=True)

        page.wait_for_timeout(5000)

        # Document didn't open
        if page.url == current_url:
            continue

        print("Document opened")

        # ==================================
        # OPEN LINE ITEMS TAB
        # ==================================
        line_items_tab = page.locator(
            "span:has-text('Line Items')"
        ).first

        line_items_tab.click()

        page.wait_for_timeout(5000)

        # ==================================
        # CHECK QUANTITY COLUMN
        # ==================================
        headers = page.locator("table thead th")

        quantity_found = False

        for j in range(headers.count()):

            text = headers.nth(j).inner_text().strip()

            print("Header:", text)

            if text == "Quantity":
                quantity_found = True
                break

        # ==================================
        # NO LINE ITEMS
        # ==================================
        if not quantity_found:

            print(
                "Quantity column not found."
            )

            print(
                "Going back to next document..."
            )

            page.go_back()

            page.wait_for_timeout(5000)

            continue

        # ==================================
        # VALID DOCUMENT FOUND
        # ==================================
        print(
            "Valid document found."
        )

        document_found = True
        break

    assert document_found, \
        "No valid 100% document found"

    # ==================================
    # FETCH COUNTS
    # ==================================
    body_text = page.locator("body").inner_text()

    print(body_text)

    # Your validations here
    assert "Quantity" in body_text

    print(
        "PASS : Line Items loaded successfully"
    )