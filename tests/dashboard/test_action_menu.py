from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from test_data.test_data import USERNAME, PASSWORD
from config.config import LOGIN_URL

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_TC_14_verify_action_menu(page):

    page.goto(LOGIN_URL)

    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    page.wait_for_timeout(5000)

    dashboard = DashboardPage(page)

    dashboard.click_action_menu()

    assert dashboard.is_refresh_visible()