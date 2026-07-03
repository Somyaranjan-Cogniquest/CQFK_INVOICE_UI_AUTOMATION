from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_TC_03_quantity_must_not_be_zero(page):

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

    # ==================================
    # FIND VALID DOCUMENT
    # ==================================
    document_found = False
    quantity_column_index = -1

    rows = page.locator("table tbody tr")

    for i in range(rows.count()):

        rows = page.locator("table tbody tr")
        row = rows.nth(i)

        if "100%" not in row.inner_text():
            continue

        print(f"\nChecking Row {i + 1}")

        current_url = page.url

        # ==============================
        # OPEN DOCUMENT
        # ==============================
        row.locator(
            "button.dropdown-toggle"
        ).click(force=True)

        page.wait_for_timeout(1000)

        row.get_by_text(
            "View document"
        ).click(force=True)

        page.wait_for_timeout(5000)

        # Document not opened
        if page.url == current_url:
            print("Document did not open")
            continue

        print("Document opened")

        # ==============================
        # OPEN LINE ITEMS TAB
        # ==============================
        line_items_tab = page.locator(
            "span:has-text('Line Items')"
        ).first

        line_items_tab.click()

        page.wait_for_timeout(5000)

        # ==============================
        # FIND QUANTITY COLUMN
        # ==============================
        headers = page.locator(
            "table thead th"
        )

        quantity_column_index = -1

        for j in range(headers.count()):

            header_text = (
                headers.nth(j)
                .inner_text()
                .strip()
            )

            print(
                f"Header {j}: {header_text}"
            )

            if header_text == "Quantity":

                quantity_column_index = j
                break

        # ==============================
        # NO LINE ITEMS
        # ==============================
        if quantity_column_index == -1:

            print(
                "Quantity column not found."
            )

            print(
                "Going back to next document..."
            )

            page.go_back()

            page.wait_for_timeout(5000)

            continue

        # ==============================
        # VALID DOCUMENT FOUND
        # ==============================
        print(
            "Valid document found."
        )

        document_found = True
        break

    assert document_found, \
        "No 100% document with line items found"

    print(
        f"Quantity column index = "
        f"{quantity_column_index}"
    )

    # ==================================
    # VALIDATE QUANTITY VALUES
    # ==================================
    rows = page.locator(
        "table tbody tr"
    )

    total_rows = rows.count()

    print(
        f"Total Line Item Rows = "
        f"{total_rows}"
    )

    validated_rows = 0

    for i in range(total_rows):

        row = rows.nth(i)

        cells = row.locator("td")

        if cells.count() <= quantity_column_index:
            continue

        quantity_input = (
            cells.nth(quantity_column_index)
            .locator("input")
        )

        if quantity_input.count() == 0:
            continue

        quantity_text = (
            quantity_input.first
            .input_value()
            .strip()
        )

        if quantity_text == "":
            continue

        print(
            f"Row {i + 1} "
            f"Quantity = {quantity_text}"
        )

        try:
            quantity_value = float(
                quantity_text.replace(",", "")
            )

        except ValueError:

            print(
                f"Skipping non numeric value : "
                f"{quantity_text}"
            )
            continue

        assert quantity_value != 0, \
            (
                f"Quantity is 0 in "
                f"Row {i + 1}"
            )

        validated_rows += 1

    assert validated_rows > 0, \
        "No Quantity values found"

    print(
        f"Validated "
        f"{validated_rows} Quantity values"
    )

    print(
        "PASS : All Quantity values "
        "are greater than 0"
    )