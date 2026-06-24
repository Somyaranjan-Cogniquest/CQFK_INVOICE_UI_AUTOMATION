from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.smoke
@pytest.mark.regression
def test_TC_25_verify_navigation_to_model_details_page(page):

    page.goto(LOGIN_URL)

    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    page.wait_for_timeout(5000)

    dashboard = DashboardPage(page)

    # Step 1: Dashboard -> TAAS
    dashboard.click_taas()

    page.wait_for_timeout(5000)

    # Step 2: Processing Dashboard -> TAAS (LUY)
    dashboard.click_taas_luy()

    page.wait_for_timeout(3000)

    # Step 3: Verify 4 cards
    assert dashboard.is_configure_model_visible()
    assert dashboard.is_training_visible()
    assert dashboard.is_processing_dashboard_visible()
    assert dashboard.is_document_analytics_visible()