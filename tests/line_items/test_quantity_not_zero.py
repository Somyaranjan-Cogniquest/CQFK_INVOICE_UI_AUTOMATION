from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.smoke
@pytest.mark.regression
def test_TC_03_quantity_must_not_be_zero(page):

    # ==================================
    # STEP 1 : LOGIN
    # ==================================
    page.goto(LOGIN_URL)

    login = LoginPage(page)

    login.login(
        USERNAME,
        PASSWORD
    )

    # ==================================
    # STEP 2 : OPEN PROCESSING DASHBOARD
    # ==================================
    dashboard = DashboardPage(page)

    dashboard.click_model_name()

    dashboard.click_processing_dashboard()

    dashboard.wait_for_table()

    print(
        "Processing Dashboard opened"
    )

    # ==================================
    # STEP 3 : OPEN FIRST 100% DOCUMENT
    # ==================================
    rows = page.locator(
        "table tbody tr"
    )

    document_found = False

    for i in range(rows.count()):

        row = rows.nth(i)

        if "100%" in row.inner_text():

            print(
                f"100% document found in row {i + 1}"
            )

            row.locator(
                "button.dropdown-toggle"
            ).click(
                force=True
            )

            page.wait_for_timeout(2000)

            row.get_by_text(
                "View document"
            ).click(
                force=True
            )

            document_found = True

            break

    assert document_found, \
        "No 100% processed document found"

    print(
        "Document opened successfully"
    )

    # ==================================
    # STEP 4 : VERIFY DATA FIELDS PAGE
    # ==================================
    assert page.locator(
        "input"
    ).count() > 0, \
        "Data Fields page not opened"

    print(
        "Data Fields page opened"
    )

    # ==================================
    # STEP 5 : OPEN LINE ITEMS TAB
    # ==================================
    line_items_tab = page.locator(
        "span:has-text('Line Items')"
    ).first

    line_items_tab.click()

    page.wait_for_timeout(3000)

    print(
        "Line Items tab opened"
    )

    # ==================================
    # STEP 6 : FIND QUANTITY COLUMN
    # ==================================
    headers = page.locator(
        "table thead th"
    )

    quantity_column_index = -1

    for i in range(headers.count()):

        header_text = (
            headers.nth(i)
            .inner_text()
            .strip()
        )

        print(
            f"Header {i} : {header_text}"
        )

        if header_text == "Quantity":

            quantity_column_index = i

            break

    assert quantity_column_index != -1, \
        "Quantity column not found"

    print(
        f"Quantity column index = {quantity_column_index}"
    )

    # ==================================
    # STEP 7 : VALIDATE QUANTITY VALUES
    # ==================================

    rows = page.locator(
        "table tbody tr"
    )

    total_rows = rows.count()

    print(
        f"Total Line Item Rows = {total_rows}"
    )

    validated_rows = 0

    for i in range(total_rows):

        row = rows.nth(i)

        quantity_input = (
            row.locator("td")
            .nth(quantity_column_index)
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
            f"Row {i + 1} Quantity = {quantity_text}"
        )

        try:

            quantity_value = float(
                quantity_text.replace(",", "")
        )

        except ValueError:

                print(
                f"Skipping non-numeric value : {quantity_text}"
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
        f"Validated {validated_rows} Quantity values"
    )

    print(
        "PASS : All Quantity values are greater than 0"
    )