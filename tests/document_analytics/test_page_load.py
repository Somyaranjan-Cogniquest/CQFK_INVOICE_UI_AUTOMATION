from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.smoke
@pytest.mark.regression
def test_TC_48_verify_document_analytics_page_load(page):

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

    page.wait_for_timeout(5000)

    print("Current URL after model click:", page.url)

    # ==========================
    # CLICK TAAS (LUY) IF PRESENT
    # ==========================
    taas = page.locator("span:has-text('TAAS')")

    print("TAAS Count:", taas.count())

    if taas.count() > 0:
        taas.first.click(force=True)
        page.wait_for_timeout(3000)

    print("URL after TAAS click:", page.url)

    # ==========================
    # FIND DOCUMENT ANALYTICS CARD
    # ==========================
    cards = page.locator("p.card-title")

    print("Cards Found:", cards.count())

    for i in range(cards.count()):
        print("Card:", cards.nth(i).text_content())

    analytics_card = page.locator(
        "p.card-title:has-text('Document Analytics')"
    )

    assert analytics_card.count() > 0, \
        "Document Analytics card not found"

    analytics_card.first.click()

    page.wait_for_timeout(5000)

    # ==========================
    # VERIFY PAGE LOADED
    # ==========================
    analytics_header = page.locator(
        "span:has-text('Document volume over time')"
    )

    assert analytics_header.is_visible(), \
        "Document Analytics page did not load"

    print("✅ Document Analytics page loaded successfully")