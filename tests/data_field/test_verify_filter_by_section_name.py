from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_TC_95_verify_filter_by_section_name(page):

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

    # ==================================
    # STEP 5 : OPEN FILTER
    # ==================================
    filter_button = page.locator(
        "button:has-text('Filter')"
    )

    filter_button.click()

    page.wait_for_timeout(2000)

    print("Filter Popup Opened")

    # ==================================
    # STEP 6 : SELECT SECTION FILTER
    # ==================================
    section_dropdown = page.locator(
        "input.ant-select-selection-search-input"
    ).first

    section_dropdown.click()

    page.wait_for_timeout(1000)

    page.keyboard.press("Enter")

    page.wait_for_timeout(2000)

    print("Section Selected")

    # ==================================
    # STEP 7 : SEARCH FIELD
    # ==================================
    field_search = page.locator(
        "input[placeholder='Field Search']"
    )

    field_search.fill(
        "Invoice Number"
    )

    page.wait_for_timeout(3000)

    print("Field Search Applied")

    # ==================================
    # STEP 8 : VERIFY FIELD DISPLAYED
    # ==================================
    invoice_number = page.locator(
        "text=Invoice Number"
    )

    assert invoice_number.first.is_visible(), \
        "Invoice Number field not found after filter"

    print(
        "PASS : Filter successfully displayed Invoice Number field"
    )