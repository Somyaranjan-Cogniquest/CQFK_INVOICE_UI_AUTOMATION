from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_TC_50_verify_document_analytics_filters(page):

    # ==========================
    # LOGIN
    # ==========================
    page.goto(LOGIN_URL)

    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    page.wait_for_timeout(5000)

    # ==========================
    # OPEN MODEL
    # ==========================
    dashboard = DashboardPage(page)

    dashboard.click_model_name()

    page.wait_for_timeout(3000)

    # ==========================
    # CLICK TAAS (LUY)
    # ==========================
    page.locator("span.Noto").filter(
        has_text="TAAS"
    ).first.click(force=True)

    page.wait_for_timeout(3000)

    # ==========================
    # OPEN DOCUMENT ANALYTICS
    # ==========================
    page.locator(
        "p.card-title:has-text('Document Analytics')"
    ).click(force=True)

    page.wait_for_timeout(5000)

    # ==========================
    # VERIFY PAGE LOADED
    # ==========================
    assert page.locator(
        "span:has-text('Document volume over time')"
    ).is_visible()

    # ==========================
    # DATE FILTER
    # ==========================
    page.locator("img.datepick").click()

    page.wait_for_timeout(2000)

    # Select start date
    page.locator(".rmdp-day").nth(5).click()

    page.wait_for_timeout(1000)

    # Select end date
    page.locator(".rmdp-day").nth(10).click()

    page.wait_for_timeout(3000)

    print("Date filter applied")

    # ==========================
    # STATUS FILTER → Approved
    # ==========================
    page.locator("div[role='combobox']").filter(
        has_text="By status"
    ).click()

    page.wait_for_timeout(1000)

    page.locator(
        "li[data-value='Approved']"
    ).click()

    page.wait_for_timeout(3000)

    print("Status filter applied")

    # ==========================
    # FLAG FILTER → Green
    # ==========================
    page.locator("div[role='combobox']").filter(
        has_text="By flags"
    ).click()

    page.wait_for_timeout(1000)

    page.locator(
        "li[data-value='Green']"
    ).click()

    page.wait_for_timeout(3000)

    print("Flag filter applied")

    # ==========================
    # VERIFY CARDS STILL VISIBLE
    # ==========================
    assert page.locator(
        "p:has-text('Total documents')"
    ).is_visible()

    assert page.locator(
        "p:has-text('Daily average')"
    ).is_visible()

    print("Cards updated after filters")

    # ==========================
    # CLEAR FILTERS
    # ==========================
    page.get_by_text("Clear filters").click()

    page.wait_for_timeout(3000)

    print("Clear Filters clicked")

    # ==========================
    # VERIFY PAGE RESTORED
    # ==========================
    assert page.locator(
        "span:has-text('Document volume over time')"
    ).is_visible()

    print("TC_50 PASSED")