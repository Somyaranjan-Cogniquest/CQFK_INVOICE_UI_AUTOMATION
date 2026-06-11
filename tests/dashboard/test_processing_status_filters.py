from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def test_TC_34_processing_status_filters(page):

    page.goto(LOGIN_URL)

    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    page.wait_for_timeout(5000)

    dashboard = DashboardPage(page)

    dashboard.click_model_name()
    dashboard.click_processing_dashboard()

    page.wait_for_timeout(3000)

    statuses = [
        "Processed",
        "Unprocessed"
    ]

    for status in statuses:

        dashboard.open_doc_status_dropdown()

        dashboard.select_doc_status(status)

        page.wait_for_timeout(3000)

        rows = page.locator("table tbody tr")
        row_count = rows.count()

        total_docs = dashboard.get_total_documents_count()

        processed = dashboard.get_processed_count()

        unprocessed = dashboard.get_unprocessed_count()

        # Validation based on selected filter
        if status == "Processed":
            assert processed == total_docs, (
                f"Processed count ({processed}) does not match Total Documents ({total_docs})"
            )

        elif status == "Unprocessed":
            assert unprocessed == total_docs, (
                f"Unprocessed count ({unprocessed}) does not match Total Documents ({total_docs})"
            )

        # Verify records are displayed
        assert row_count > 0, f"No records found for {status}"