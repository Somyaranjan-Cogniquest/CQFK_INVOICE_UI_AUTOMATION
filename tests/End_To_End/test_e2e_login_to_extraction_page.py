from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.smoke
@pytest.mark.sanity
@pytest.mark.regression
def test_E2E_01_login_to_extraction_page(page):

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

    print("Dashboard loaded successfully")

    # ==================================
    # STEP 3 : OPEN PROCESSING DASHBOARD
    # ==================================
    dashboard.click_processing_dashboard()

    assert "/document" in page.url, \
        "Processing Dashboard not opened"

    print("Processing Dashboard opened")

    # ==================================
    # STEP 4 : WAIT FOR TABLE
    # ==================================
    dashboard.wait_for_table()

    rows = page.locator("table tbody tr")

    total_rows = rows.count()

    document_found = False

    for i in range(total_rows):

        row = rows.nth(i)

        if "100%" in row.inner_text():

            menu_button = row.locator(
                "button.dropdown-toggle"
            )

            if menu_button.count() > 0:

                menu_button.first.click(force=True)

                page.wait_for_timeout(2000)

                view_document = row.locator(
                    "a.dropdown-item"
                ).filter(has_text="View document")

                if view_document.count() > 0:

                    view_document.first.click(
                        force=True
                    )

                    document_found = True

                    print(
                        f"Opened document from row {i + 1}"
                    )

                    break

    assert document_found, \
        "No 100% processed document found"

    # ==================================
    # STEP 5 : VERIFY EXTRACTION PAGE
    # ==================================
    page.wait_for_load_state("networkidle")

    current_url = page.url

    print("Current URL :", current_url)

    # PDF Viewer Validation
    pdf_present = (
        page.locator("canvas").count() > 0
        or
        page.locator("iframe").count() > 0
    )

    assert pdf_present, \
        "PDF Viewer not visible"

    print("PDF Viewer visible")

    # Extracted Fields Validation
    extracted_fields = page.locator("input").count()

    assert extracted_fields > 0, \
        "Extracted fields not visible"

    print("Extracted fields visible")

    # Line Items Validation
    assert page.get_by_text(
        "Line Items"
    ).count() > 0, \
        "Line Items section not visible"

    print("Line Items section visible")

    print(
        "PASS : E2E_01 Login → Dashboard → Processing Dashboard → View Document → Extraction Page"
    )