from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_TC_36_verify_table_headers(page):

    page.goto(LOGIN_URL)

    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    page.wait_for_timeout(5000)

    dashboard = DashboardPage(page)

    dashboard.click_model_name()
    dashboard.click_processing_dashboard()

    page.wait_for_timeout(3000)

    expected_headers = [
        "Sl.",
        "Doc ID",
        "Document Name",
        "Uploaded",
        "Last Processed",
        "Processing",
        "Data Fields",
        "Line items",
        "Action"
    ]

    actual_headers = []

    headers = page.locator("table thead th")

    for i in range(headers.count()):
        actual_headers.append(
            headers.nth(i).inner_text().strip()
        )

    assert actual_headers == expected_headers, (
        f"\nExpected: {expected_headers}"
        f"\nActual: {actual_headers}"
    )