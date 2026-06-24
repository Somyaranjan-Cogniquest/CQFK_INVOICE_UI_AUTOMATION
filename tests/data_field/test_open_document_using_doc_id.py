from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.smoke
@pytest.mark.regression
def test_TC_93_verify_document_opens_using_doc_id(page):

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
    # STEP 5 : VERIFY DOC ID FIELD
    # ==================================
    doc_id_field = page.locator(
        "input[placeholder='Enter Doc ID']"
    )

    assert doc_id_field.is_visible(), \
        "Doc ID field not visible"

    current_doc_id = doc_id_field.input_value()

    print(
        f"Current Doc ID : {current_doc_id}"
    )

    # ==================================
    # STEP 6 : OPEN PREVIOUS DOCUMENT
    # ==================================
    previous_button = page.locator(
        "button:has(img[src*='back_icon'])"
    )

    previous_button.click()

    page.wait_for_timeout(5000)

    previous_doc_id = doc_id_field.input_value()

    print(
        f"Previous Doc ID : {previous_doc_id}"
    )

    assert previous_doc_id != current_doc_id, \
        "Previous document did not open"

    # ==================================
    # STEP 7 : ENTER DOC ID MANUALLY
    # ==================================
    doc_id_field.fill("")

    doc_id_field.fill(previous_doc_id)

    page.keyboard.press("Enter")

    page.wait_for_timeout(5000)

    # ==================================
    # STEP 8 : VERIFY DOCUMENT OPENED
    # ==================================
    opened_doc_id = doc_id_field.input_value()

    print(
        f"Opened Doc ID : {opened_doc_id}"
    )

    assert opened_doc_id == previous_doc_id, \
        "Document did not open using Doc ID"

    # ==================================
    # STEP 9 : VERIFY PAGE LOADED
    # ==================================
    invoice_details = page.locator(
        "span[title='Invoice Details']"
    )

    assert invoice_details.is_visible(), \
        "Invoice Details not visible"

    print(
        "PASS : Document opened successfully using Doc ID search"
    )