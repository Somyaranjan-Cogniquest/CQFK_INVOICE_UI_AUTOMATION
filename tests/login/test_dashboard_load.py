from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
import pytest

@pytest.mark.smoke
@pytest.mark.regression
def test_TC_10_dashboard_load(page):

    page.goto(LOGIN_URL)

    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    page.wait_for_url("**/dashboard")

    dashboard = DashboardPage(page)

    assert dashboard.is_home_visible()