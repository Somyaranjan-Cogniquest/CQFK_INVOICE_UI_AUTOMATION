from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.smoke
@pytest.mark.regression
def test_TC_44_search_by_doc_id(page):

    # ==========================
    # LOGIN
    # ==========================
    page.goto(LOGIN_URL)

    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    page.wait_for_timeout(5000)

    # ==========================
    # NAVIGATE TO DASHBOARD
    # ==========================
    dashboard = DashboardPage(page)
    dashboard.click_model_name()
    dashboard.click_processing_dashboard()

    page.wait_for_timeout(5000)

    # ==========================
    # SEARCH DOC ID
    # ==========================
    doc_id = "71460"

    search_box = page.locator("input.searchbar")
    search_box.fill(doc_id)

    page.wait_for_timeout(3000)

    # ==========================
    # VERIFY SEARCH RESULT
    # ==========================
    result = page.locator(f"text={doc_id}")

    assert result.first.is_visible(), f"Doc ID {doc_id} not found in results"

    print(f"✅ Search successful. Doc ID {doc_id} displayed.")