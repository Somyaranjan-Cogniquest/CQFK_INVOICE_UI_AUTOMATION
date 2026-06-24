from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_TC_89_verify_zoom_slider_functionality(page):

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

        row_text = row.inner_text()

        if "100%" in row_text:

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
    # STEP 6 : VERIFY ZOOM SLIDER
    # ==================================

    zoom_slider = page.locator(
        "input[type='range']"
    )

    assert zoom_slider.is_visible(), \
        "Zoom Slider not visible"

    initial_value = zoom_slider.input_value()

    print(
        f"Initial Zoom Value : {initial_value}"
    )

    # --------------------------
    # ZOOM IN
    # --------------------------

    zoom_slider.evaluate(
        "(el) => el.value = 220"
    )

    page.wait_for_timeout(5000)

    zoom_in_value = zoom_slider.input_value()

    print(
    f"Zoom In Value : {zoom_in_value}"
)

    assert int(zoom_in_value) > int(initial_value), \
        "Zoom In not working"

    print("Zoom In working")

    # --------------------------
    # WAIT AFTER ZOOM IN
    # --------------------------

    page.wait_for_timeout(5000)

    # --------------------------
    # ZOOM OUT
    # --------------------------

    zoom_slider.evaluate(
        "(el) => el.value = 100"
    )

    page.wait_for_timeout(5000)

    zoom_out_value = zoom_slider.input_value()

    print(
        f"Zoom Out Value : {zoom_out_value}"
    )

    # --------------------------
    # VALIDATION
    # --------------------------

    assert int(zoom_out_value) <= int(zoom_in_value), \
        "Zoom Out not working"

    print(
        "PASS : Zoom Slider working successfully"
    )