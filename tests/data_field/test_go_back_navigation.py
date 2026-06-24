from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.smoke
@pytest.mark.regression
def test_TC_98_verify_go_back_navigation(page):

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
    # STEP 4 : OPEN FIRST 100% DOCUMENT
    # ==================================
    rows = page.locator(
        "table tbody tr"
    )

    total_rows = rows.count()

    document_opened = False

    for i in range(total_rows):

        row = rows.nth(i)

        if "100%" in row.inner_text():

            menu_button = row.locator(
                "button.dropdown-toggle"
            )

            menu_button.first.click(
                force=True
            )

            page.wait_for_timeout(2000)

            view_document = row.locator(
                "a[title='View Document']"
            )

            if view_document.count() > 0:

                view_document.first.click(
                    force=True
                )

                document_opened = True

                break

    assert document_opened, \
        "No 100% processed document found"

    print("Data Field Page Opened")
    page.wait_for_timeout(5000)


    # ==================================
    # STEP 5 : VERIFY DATA FIELD PAGE
    # ==================================
    invoice_details = page.locator(
        "span[title='Invoice Details']"
    )

    assert invoice_details.is_visible(), \
        "Invoice Details section not visible"

    print("Invoice Details Visible")

    # ==================================
    # STEP 6 : CLICK GO BACK BUTTON
    # ==================================
    go_back_button = page.locator(
        "[data-testid='ArrowLeftIcon']"
    )

    assert go_back_button.is_visible(), \
        "Go Back button not visible"

    go_back_button.click()

    page.wait_for_timeout(5000)

    # ==================================
    # STEP 7 : VERIFY PROCESSING DASHBOARD
    # ==================================
    assert "/document" in page.url, \
        "Processing Dashboard not opened"

    table_rows = page.locator(
        "table tbody tr"
    )

    assert table_rows.count() > 0, \
        "Documents table not visible"

    print(
        "PASS : Go Back redirected to Processing Dashboard successfully"
    )