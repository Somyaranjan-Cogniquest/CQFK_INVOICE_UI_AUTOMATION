from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def test_TC_38A_current_month_date_filter(page):

    page.goto(LOGIN_URL)

    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    page.wait_for_timeout(5000)

    dashboard = DashboardPage(page)

    dashboard.click_model_name()
    dashboard.click_processing_dashboard()

    page.wait_for_timeout(3000)

    # Open calendar
    page.locator("img.datepick").click()

    page.wait_for_timeout(1000)

    # Select start date
    page.get_by_role("cell", name="1", exact=True).click()

    page.wait_for_timeout(1000)

# Select end date
    page.get_by_role("cell", name="10", exact=True).click()
    page.wait_for_timeout(3000)

    rows = page.locator("table tbody tr")

    assert rows.count() > 0, "No documents displayed after date filter"