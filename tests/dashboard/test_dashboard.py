from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from config.config import LOGIN_URL, DASHBOARD_URL
from test_data.test_data import USERNAME, PASSWORD


def test_TC_11_verify_model_table_headers(page):

    page.goto(LOGIN_URL)

    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    page.wait_for_url("**/dashboard", timeout=20000)

    dashboard = DashboardPage(page)

    actual_headers = dashboard.get_header_text_list()

    expected_headers = [
        "Sl.",
        "Model Name",
        "Model ID",
        "Date Created",
        "Last Updated",
        "Trained",
        "Trained Count",
        "Action"
    ]

    print("Actual Headers:", actual_headers)

    assert actual_headers == expected_headers