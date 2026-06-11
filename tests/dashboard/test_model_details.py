from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def test_TC_28_processing_dashboard_card_visibility(page):

    page.goto(LOGIN_URL)

    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    page.wait_for_timeout(5000)

    dashboard = DashboardPage(page)

    dashboard.click_model_name()

    assert dashboard.is_processing_dashboard_visible()

    assert dashboard.is_processing_dashboard_clickable()

    dashboard.click_processing_dashboard()