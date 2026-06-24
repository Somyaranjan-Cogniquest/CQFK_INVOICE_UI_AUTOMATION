from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_TC_37_search_functionality(page):

    page.goto(LOGIN_URL)

    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    page.wait_for_timeout(5000)

    dashboard = DashboardPage(page)

    dashboard.click_model_name()
    dashboard.click_processing_dashboard()

    page.wait_for_timeout(3000)

    # -------------------------
    # Search By Doc ID
    # -------------------------

    doc_id = dashboard.get_first_doc_id()

    dashboard.search_document(doc_id)

    rows = page.locator("table tbody tr")

    assert rows.count() > 0

    for i in range(rows.count()):
        row_text = rows.nth(i).inner_text()
        assert doc_id in row_text

    # Clear Search
    dashboard.search_document("")

    page.wait_for_timeout(2000)

    # -------------------------
    # Search By Document Name
    # -------------------------

    doc_name = dashboard.get_first_document_name()

    partial_name = doc_name[:5]

    dashboard.search_document(partial_name)

    rows = page.locator("table tbody tr")

    assert rows.count() > 0

    for i in range(rows.count()):
        row_text = rows.nth(i).inner_text().lower()

        assert partial_name.lower() in row_text