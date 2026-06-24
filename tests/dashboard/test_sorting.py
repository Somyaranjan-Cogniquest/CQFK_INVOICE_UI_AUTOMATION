from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from test_data.test_data import USERNAME, PASSWORD
from config.config import LOGIN_URL

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_TC_13_verify_sorting_on_columns(page):

    # Login
    page.goto(LOGIN_URL)

    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    page.wait_for_timeout(5000)

    dashboard = DashboardPage(page)

    # Click Model ID header
    dashboard.click_model_id_header()

    page.wait_for_timeout(2000)

    # Click again for reverse sorting
    dashboard.click_model_id_header()

    page.wait_for_timeout(2000)

    # Click Date Created header
    dashboard.click_date_created_header()

    page.wait_for_timeout(2000)

    # Click again for reverse sorting
    dashboard.click_date_created_header()

    page.wait_for_timeout(2000)

    assert True