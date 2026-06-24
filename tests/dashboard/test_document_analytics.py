from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.smoke
@pytest.mark.regression
def test_TC_29_document_analytics_visibility(page):

    # Open login page
    page.goto(LOGIN_URL)

    # Login
    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    # IMPORTANT: same stable wait as TC_28
    page.wait_for_timeout(5000)

    # Dashboard page object
    dashboard = DashboardPage(page)

    # Same step as working test
    dashboard.click_model_name()

    # IMPORTANT: add small wait after model load
    page.wait_for_timeout(3000)

    # FINAL FIX: visibility check with safety wait inside method
    assert dashboard.is_document_analytics_visible()