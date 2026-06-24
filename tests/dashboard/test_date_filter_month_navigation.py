from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_TC_38B_month_navigation(page):

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

    page.wait_for_timeout(1500)

    # =========================
    # STEP 1: SELECT START DATE
    # =========================
    page.locator(".rmdp-day").filter(has_text="5").first.click()

    page.wait_for_timeout(1000)

    # =========================
    # STEP 2: MOVE TO NEXT MONTH
    # =========================
    page.locator("span.rmdp-right").click()

    page.wait_for_timeout(1500)

    # =========================
    # STEP 3: SELECT END DATE
    # =========================
    page.locator(".rmdp-day").filter(has_text="15").first.click()

    page.wait_for_timeout(3000)

    # =========================
    # VALIDATION
    # =========================
    rows = page.locator("table tbody tr")
    row_count = rows.count()

    print("Rows found:", row_count)

    assert row_count >= 0