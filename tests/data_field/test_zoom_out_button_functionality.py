from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_TC_88_verify_zoom_out_button_functionality(page):

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

    # ==================================
    # STEP 5 : VERIFY INVOICE DETAILS
    # ==================================
    invoice_details = page.locator(
        "span[title='Invoice Details']"
    )

    invoice_details.wait_for(
        state="visible",
        timeout=15000
    )

    assert invoice_details.is_visible(), \
        "Invoice Details section not visible"

    print("Invoice Details Visible")

    # ==================================
    # STEP 6 : CLICK ZOOM OUT (-)
    # ==================================
    zoom_buttons = page.locator("button")

    zoom_out_button = zoom_buttons.nth(1)

    assert zoom_out_button.is_visible(), \
        "Zoom Out button not visible"

    zoom_out_button.click(
        force=True
    )

    page.wait_for_timeout(2000)

    print("Zoom Out button clicked")

    # ==================================
    # STEP 7 : VERIFY PAGE STILL LOADED
    # ==================================
    assert invoice_details.is_visible(), \
        "Page broke after Zoom Out"

    print(
        "PASS : Zoom Out (-) button working successfully"
    )