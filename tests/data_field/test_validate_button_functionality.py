from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.smoke
@pytest.mark.sanity
@pytest.mark.regression
def test_TC_96_verify_validate_button_functionality(page):

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
    # STEP 5 : VERIFY VALIDATE BUTTON
    # ==================================
    validate_button = page.locator(
        "button:has-text('Validate')"
    )

    assert validate_button.is_visible(), \
        "Validate button not visible"

    print("Validate Button Visible")

    # ==================================
    # STEP 6 : CLICK VALIDATE
    # ==================================
    validate_button.click()

    print("Validate Button Clicked")

    page.wait_for_timeout(5000)

    # ==================================
    # STEP 7 : VERIFY SUCCESS MESSAGE
    # ==================================
    success_message = page.locator(
        "text=Data validated successfully"
    )

    success_message.wait_for(
        state="visible",
        timeout=15000
    )

    assert success_message.is_visible(), \
        "Validation success message not displayed"

    print(
        "PASS : Data validated successfully"
    )