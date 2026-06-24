from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.smoke
@pytest.mark.regression
def test_TC_91_verify_previous_document_navigation(page):

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
    # STEP 6 : CLICK PREVIOUS BUTTON
    # ==================================
    
    previous_button = page.locator(
        "button:has(img[src*='back_icon'])"
    )

    assert previous_button.is_visible(), \
        "Previous button not visible"

    doc_id_before = page.locator(
        "input[placeholder='Enter Doc ID']"
    ).input_value()

    print(f"Current Doc ID : {doc_id_before}")

    previous_button.click()

    page.wait_for_timeout(5000)

    doc_id_after = page.locator(
        "input[placeholder='Enter Doc ID']"
    ).input_value()

    print(f"Previous Doc ID : {doc_id_after}")

    assert doc_id_before != doc_id_after, \
        "Previous document not opened"

    print("PASS : Previous document opened successfully")