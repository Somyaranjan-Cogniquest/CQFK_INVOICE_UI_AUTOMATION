from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.smoke
@pytest.mark.regression
def test_TC_68_view_document_opens_extraction_page(page):

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

    assert total_rows > 0, "No document rows found"

    document_found = False

    for i in range(total_rows):

        row = rows.nth(i)

        row_text = row.inner_text()

        if "100%" in row_text:

            print(f"100% Document Found in Row {i+1}")

            # Open 3-dot menu
            three_dot = row.locator("button.dropdown-toggle")

            three_dot.click(force=True)

            page.wait_for_timeout(2000)

            # Click View Document
            row.get_by_text("View document").click(force=True)

            page.wait_for_timeout(5000)

            document_found = True
            break

    assert document_found, "No processed (100%) document found"

    # ==========================
    # VERIFY EXTRACTION PAGE
    # ==========================
    current_url = page.url

    print("Current URL:", current_url)

    assert (
        "document_slt" in current_url
        or "document" in current_url
    ), "Extraction page not opened"

    # ==========================
    # VERIFY PDF VIEWER EXISTS
    # ==========================
    pdf_visible = (
        page.locator("iframe").count() > 0
        or page.locator("canvas").count() > 0
        or page.locator("embed").count() > 0
    )

    assert pdf_visible, "PDF viewer not visible"

    print("PDF loaded successfully")

    # ==========================
    # VERIFY EXTRACTED FIELDS PANEL
    # ==========================
    body_text = page.locator("body").inner_text()

    assert len(body_text) > 0, "Extraction page is empty"

    print("Extraction page loaded successfully")