from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_TC_47_verify_data_fields_responsiveness(page):

    # ==========================
    # LOGIN
    # ==========================
    page.goto(LOGIN_URL)

    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    page.wait_for_timeout(5000)

    # ==========================
    # NAVIGATE TO PROCESSING DASHBOARD
    # ==========================
    dashboard = DashboardPage(page)

    dashboard.click_model_name()
    dashboard.click_processing_dashboard()

    page.wait_for_timeout(5000)

    # ==========================
    # OPEN FIRST 100% DOCUMENT
    # ==========================
    rows = page.locator("table tbody tr")

    document_clicked = False

    for i in range(rows.count()):

        row = rows.nth(i)

        if row.locator("text=100%").count() > 0:

            document = row.locator("div[docid]").first

            document.scroll_into_view_if_needed()
            document.click(force=True)

            document_clicked = True
            break

    assert document_clicked, "No 100% processed document found"

    page.wait_for_timeout(5000)

    # ==========================
    # DESKTOP VIEW
    # ==========================
    page.set_viewport_size({"width": 1920, "height": 1080})

    page.wait_for_timeout(2000)

    assert page.locator("body").is_visible()

    print("Desktop view validated")

    # ==========================
    # LAPTOP VIEW
    # ==========================
    page.set_viewport_size({"width": 1366, "height": 768})

    page.wait_for_timeout(2000)

    assert page.locator("body").is_visible()

    print("Laptop view validated")

    # ==========================
    # TABLET VIEW
    # ==========================
    page.set_viewport_size({"width": 768, "height": 1024})

    page.wait_for_timeout(2000)

    assert page.locator("body").is_visible()

    print("Tablet view validated")

    # ==========================
    # MOBILE VIEW
    # ==========================
    page.set_viewport_size({"width": 390, "height": 844})

    page.wait_for_timeout(2000)

    assert page.locator("body").is_visible()

    print("Mobile view validated")

