from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def test_TC_33_review_status_filters(page):

    page.goto(LOGIN_URL)

    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    page.wait_for_timeout(5000)

    dashboard = DashboardPage(page)

    dashboard.click_model_name()
    dashboard.click_processing_dashboard()

    page.wait_for_timeout(3000)

    statuses = [
        "Approved",
        "Not approved",
        "Rejected",
        "Deleted"
    ]

    for status in statuses:

        dashboard.open_review_status_dropdown()

        dashboard.select_review_status(status)

        page.wait_for_timeout(3000)

        rows = page.locator("table tbody tr")

        actual_count = rows.count()

        print(f"Filter: {status}")
        print(f"Visible rows: {actual_count}")

        if status in ["Rejected", "Deleted"]:
            print(f"{status} has {actual_count} records")
        else:
            assert actual_count > 0, f"No records found for {status}"