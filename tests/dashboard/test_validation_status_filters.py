from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_TC_35_color_status_filters(page):

    page.goto(LOGIN_URL)

    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    page.wait_for_timeout(5000)

    dashboard = DashboardPage(page)

    dashboard.click_model_name()
    dashboard.click_processing_dashboard()

    page.wait_for_timeout(3000)

    colors = [
        "Green",
        "Red"
    ]

    for color in colors:

        dashboard.open_color_status_dropdown()

        dashboard.select_color_status(color)

        page.wait_for_timeout(3000)

        rows = page.locator("table tbody tr")
        row_count = rows.count()

        total_docs = dashboard.get_total_documents_count()

        # Validation
        assert row_count > 0, f"No records found for {color}"

        # Optional verification
        assert total_docs >= row_count

        print(
            f"{color} Filter Applied | "
            f"Rows: {row_count} | "
            f"Total Documents: {total_docs}"
        )