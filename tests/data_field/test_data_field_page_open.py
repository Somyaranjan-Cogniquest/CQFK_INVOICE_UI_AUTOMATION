from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.smoke
@pytest.mark.regression
def test_TC_86_verify_data_field_page_opens_for_processed_document(page):

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
    # STEP 2 : OPEN MODEL
    # ==================================
    dashboard = DashboardPage(page)

    dashboard.click_model_name()

    print("Model Landing Page Opened")

    # ==================================
    # STEP 3 : OPEN PROCESSING DASHBOARD
    # ==================================
    dashboard.click_processing_dashboard()

    dashboard.wait_for_table()

    print("Processing Dashboard Opened")

    # ==================================
    # STEP 4 : FIND FIRST 100% DOCUMENT
    # ==================================
    rows = page.locator(
        "table tbody tr"
    )

    total_rows = rows.count()

    document_opened = False

    for i in range(total_rows):

        row = rows.nth(i)

        row_text = row.inner_text()

        if "100%" in row_text:

            print(
                f"100% Processed Document Found : Row {i + 1}"
            )

            # Open 3-dot menu
            menu_button = row.locator(
                "button.dropdown-toggle"
            )

            menu_button.first.click(
                force=True
            )

            page.wait_for_timeout(2000)

            # Click View Document from same row
            view_document = row.locator(
                "a[title='View Document']"
            )

            if view_document.count() > 0:

                view_document.first.click(
                    force=True
                )

                document_opened = True

                print(
                    "View Document clicked successfully"
                )

                break

    assert document_opened, \
        "No 100% processed document found"

    # ==================================
    # STEP 5 : VERIFY DATA FIELD PAGE
    # ==================================
    page.wait_for_timeout(5000)

    invoice_details = page.locator(
        "span[title='Invoice Details']"
    )

    invoice_details.wait_for(
        state="visible",
        timeout=15000
    )

    assert invoice_details.is_visible(), \
        "Invoice Details section not visible"

    print(
        "PASS : Invoice Details section visible"
    )