from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_TC_44_search_by_doc_id(page):

    page.goto(LOGIN_URL)

    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    page.wait_for_timeout(5000)

    dashboard = DashboardPage(page)
    dashboard.click_model_name()
    dashboard.click_processing_dashboard()

    page.wait_for_timeout(5000)

    # Search old document
    doc_id = "71460"

    search_box = page.locator("input.searchbar")
    search_box.fill(doc_id)

    page.wait_for_timeout(1000)

    # Click Extend Search
    extend_btn = page.get_by_role(
        "button",
        name="Extend Search"
    )

    extend_btn.click()

    page.wait_for_timeout(5000)

    rows = page.locator("tbody tr")

    assert rows.count() > 0, \
        f"Doc ID {doc_id} not found"

    result = page.locator(f"text={doc_id}")

    assert result.first.is_visible(), \
        f"Doc ID {doc_id} not visible"

    print(f"✅ Search successful. Doc ID {doc_id} displayed.")