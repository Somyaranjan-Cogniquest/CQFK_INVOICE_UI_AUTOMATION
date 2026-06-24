from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.smoke
@pytest.mark.regression
def test_TC_92_verify_next_document_navigation(page):

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
    # STEP 5 : GET CURRENT DOC ID
    # ==================================
    doc_id_field = page.locator(
        "input[placeholder='Enter Doc ID']"
    )

    doc_id_before = doc_id_field.input_value()

    print(
        f"Current Doc ID : {doc_id_before}"
    )

    # ==================================
    # STEP 6 : CLICK NEXT BUTTON
    # ==================================
    next_button = page.locator(
        "button:has(img[src*='next_icon'])"
    )

    assert next_button.is_visible(), \
        "Next button not visible"

    print(
        "Next Button Enabled :",
        next_button.is_enabled()
    )

    if next_button.is_enabled():

        next_button.click()

        page.wait_for_timeout(5000)

        doc_id_after = doc_id_field.input_value()

        print(
            f"Next Doc ID : {doc_id_after}"
        )

        assert doc_id_before != doc_id_after, \
            "Next document not opened"

        print(
            "PASS : Next document opened successfully"
        )

    else:

        print(
            "PASS : Next button disabled because last document is opened"
        )