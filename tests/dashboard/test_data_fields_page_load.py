from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.smoke
@pytest.mark.regression
def test_TC_45_verify_data_fields_page_load(page):

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
    # FIND 100% PROCESSED DOCUMENT
    # ==========================
    rows = page.locator("table tbody tr")

    row_count = rows.count()

    print(f"Total Rows Found: {row_count}")

    assert row_count > 0, "No rows found in Processing Dashboard"

    current_url = page.url
    document_clicked = False

    for i in range(row_count):

        row = rows.nth(i)

        try:
            percentage = row.locator("div.sc-pyfCe").first.text_content().strip()

            print(f"Row {i+1} Processing: {percentage}")

            if percentage == "100%":

                print(f"100% Processed Document Found in Row {i+1}")

                document = row.locator("div[docid]").first

                document_name = document.text_content()

                print("Opening Document:", document_name)

                document.scroll_into_view_if_needed()

                page.wait_for_timeout(1000)

                document.click(force=True)

                document_clicked = True

                break

        except Exception as e:
            print(f"Skipping row {i+1}: {e}")

    assert document_clicked, "No document with 100% processing found"

    # ==========================
    # VERIFY DATA FIELDS PAGE OPENED
    # ==========================
    page.wait_for_timeout(5000)

    print("Current URL:", page.url)

    assert page.url != current_url, \
        "Data Fields page did not open after clicking 100% processed document"

    print("✅ Data Fields page opened successfully")