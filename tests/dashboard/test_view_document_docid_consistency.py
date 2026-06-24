from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.smoke
@pytest.mark.regression
def test_TC_78_view_document_docid_consistency(page):

    # ==========================
    # LOGIN
    # ==========================
    page.goto(LOGIN_URL)

    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    page.wait_for_timeout(5000)

    # ==========================
    # OPEN PROCESSING DASHBOARD
    # ==========================
    dashboard = DashboardPage(page)

    dashboard.click_model_name()
    dashboard.click_processing_dashboard()

    page.wait_for_timeout(5000)

    # ==========================
    # FIND FIRST 100% DOCUMENT
    # ==========================
    rows = page.locator("tbody tr")

    total_rows = rows.count()

    selected_doc_id = None

    for i in range(total_rows):

        row = rows.nth(i)

        row_text = row.inner_text()

        if "100%" in row_text:

            # Doc ID column
            selected_doc_id = (
                row.locator("td").nth(1).inner_text().strip()
            )

            print(
                f"Selected Processing Dashboard Doc ID: "
                f"{selected_doc_id}"
            )

            # Open 3-dot menu
            row.locator(
                "button.dropdown-toggle"
            ).click(force=True)

            page.wait_for_timeout(2000)

            # Click View Document
            row.get_by_text(
                "View document",
                exact=False
            ).click(force=True)

            break

    assert selected_doc_id is not None, \
        "No processed (100%) document found"

    # ==========================
    # EXTRACTION PAGE
    # ==========================
    page.wait_for_timeout(5000)

    doc_id_input = page.locator(
        "input[placeholder='Enter Doc ID']"
    )

    extraction_doc_id = (
        doc_id_input.input_value().strip()
    )

    print(
        f"Extraction Page Doc ID: "
        f"{extraction_doc_id}"
    )

    # ==========================
    # VALIDATION
    # ==========================
    assert selected_doc_id == extraction_doc_id, (
        f"Doc ID mismatch. "
        f"Dashboard={selected_doc_id}, "
        f"Extraction={extraction_doc_id}"
    )

    print(
        "PASS - Opened document matches selected Doc ID"
    )