import pytest

from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def get_doc_id_from_extraction(page):

    doc_id_input = page.locator(
        "input[placeholder='Enter Doc ID']"
    )

    return doc_id_input.input_value().strip()


@pytest.mark.smoke
@pytest.mark.regression
def test_E2E_12_view_document_doc_integrity(page):

    # ==================================
    # STEP 1 : LOGIN
    # ==================================
    page.goto(LOGIN_URL)

    login = LoginPage(page)

    login.login(
        USERNAME,
        PASSWORD
    )

    print("Login successful")

    # ==================================
    # STEP 2 : OPEN PROCESSING DASHBOARD
    # ==================================
    dashboard = DashboardPage(page)

    dashboard.click_model_name()

    dashboard.click_processing_dashboard()

    dashboard.wait_for_table()

    print("Processing Dashboard opened")

    # ==================================
    # STEP 3 : FIND FIRST 100% DOCUMENT
    # ==================================
    rows = page.locator(
        "table tbody tr"
    )

    first_doc_id = None
    first_row = None

    for i in range(rows.count()):

        row = rows.nth(i)

        if "100%" in row.inner_text():

            first_row = row

            first_doc_id = (
                row.locator("td")
                .nth(1)
                .inner_text()
                .strip()
            )

            print(
                f"First Doc ID : {first_doc_id}"
            )

            break

    assert first_doc_id is not None

    # ==================================
    # STEP 4 : OPEN FIRST DOCUMENT
    # ==================================
    first_row.locator(
        "button.dropdown-toggle"
    ).click(force=True)

    page.wait_for_timeout(2000)

    first_row.get_by_text(
        "View document"
    ).click(force=True)

    page.wait_for_timeout(5000)

    extraction_doc_id = (
        get_doc_id_from_extraction(page)
    )

    print(
        f"Extraction Doc ID : {extraction_doc_id}"
    )

    assert extraction_doc_id == first_doc_id, \
        "First document mismatch"

    print(
        "First document validated"
    )

    # ==================================
    # STEP 5 : GO BACK
    # ==================================
    page.go_back()

    dashboard.wait_for_table()

    # ==================================
    # STEP 6 : FIND SECOND 100% DOCUMENT
    # ==================================
    rows = page.locator(
        "table tbody tr"
    )

    second_doc_id = None
    second_row = None

    for i in range(rows.count()):

        row = rows.nth(i)

        if "100%" in row.inner_text():

            current_doc_id = (
                row.locator("td")
                .nth(1)
                .inner_text()
                .strip()
            )

            if current_doc_id == first_doc_id:
                continue

            second_doc_id = current_doc_id
            second_row = row

            print(
                f"Second Doc ID : {second_doc_id}"
            )

            break

    assert second_doc_id is not None

    # ==================================
    # STEP 7 : OPEN SECOND DOCUMENT
    # ==================================
    second_row.locator(
        "button.dropdown-toggle"
    ).click(force=True)

    page.wait_for_timeout(2000)

    second_row.get_by_text(
        "View document"
    ).click(force=True)

    page.wait_for_timeout(5000)

    extraction_doc_id = (
        get_doc_id_from_extraction(page)
    )

    print(
        f"Extraction Doc ID : {extraction_doc_id}"
    )

    assert extraction_doc_id == second_doc_id, \
        "Second document mismatch"

    print(
        "Second document validated"
    )

    print(
        "PASS : E2E_12 View Document Doc Integrity"
    )