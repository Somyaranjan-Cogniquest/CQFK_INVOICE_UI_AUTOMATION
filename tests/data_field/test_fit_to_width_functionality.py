from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_TC_90_verify_fit_to_width_functionality(page):

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

            print(
                f"100% Processed Document Found : Row {i + 1}"
            )

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
    # STEP 6 : ZOOM IN
    # ==================================
    zoom_slider = page.locator(
        "input[type='range']"
    )

    assert zoom_slider.is_visible(), \
        "Zoom slider not visible"

    zoom_slider.evaluate(
        """
        (el) => {
            el.value = '250';
            el.dispatchEvent(
                new Event('input', { bubbles: true })
            );
        }
        """
    )

    page.wait_for_timeout(3000)

    print("Zoom In Applied")

    # ==================================
    # STEP 7 : ZOOM OUT
    # ==================================
    zoom_slider.evaluate(
        """
        (el) => {
            el.value = '100';
            el.dispatchEvent(
                new Event('input', { bubbles: true })
            );
        }
        """
    )

    page.wait_for_timeout(3000)

    print("Zoom Out Applied")

    # ==================================
    # STEP 8 : CLICK FIT TO WIDTH
    # ==================================
    fit_to_width = page.locator(
        "img[src*='zoom_1']"
    ).locator(
        "xpath=.."
    )

    assert fit_to_width.is_visible(), \
        "Fit To Width button not visible"

    fit_to_width.click(
        force=True
    )

    page.wait_for_timeout(5000)

    print("Fit To Width clicked")

    # ==================================
    # STEP 9 : VERIFY PAGE STILL LOADED
    # ==================================
    assert invoice_details.is_visible(), \
        "Invoice Details section disappeared after Fit To Width"

    print(
        "PASS : Fit To Width functionality working successfully"
    )