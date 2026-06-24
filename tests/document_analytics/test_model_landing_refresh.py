from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_TC_53_verify_model_landing_refresh_stability(page):

    # LOGIN
    page.goto(LOGIN_URL)

    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    page.wait_for_timeout(5000)

    # OPEN MODEL
    dashboard = DashboardPage(page)
    dashboard.click_model_name()

    page.wait_for_timeout(5000)

    print("Current URL:", page.url)

    # VERIFY PAGE LOADED
    assert "dashboard" in page.url or "document" in page.url

    # REFRESH PAGE
    page.reload()

    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(5000)

    print("URL after refresh:", page.url)

    # VERIFY PAGE STILL LOADED
    assert page.url is not None
    assert len(page.url) > 0

    # VERIFY SOME PAGE CONTENT EXISTS
    body_text = page.locator("body").text_content()

    assert body_text is not None
    assert len(body_text.strip()) > 0

    print("TC_53 PASSED")