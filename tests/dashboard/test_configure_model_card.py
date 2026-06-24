from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_TC_26_verify_configure_model_card_visibility(page):

    page.goto(LOGIN_URL)

    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    page.wait_for_timeout(5000)

    dashboard = DashboardPage(page)

    dashboard.click_taas()

    page.wait_for_timeout(3000)

    dashboard.click_taas_luy()

    page.wait_for_timeout(3000)

    # Visible
    assert dashboard.is_configure_model_visible()

    # Clickable
    dashboard.click_configure_model()