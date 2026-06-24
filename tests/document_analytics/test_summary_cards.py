from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.smoke
@pytest.mark.regression
def test_TC_49_verify_document_analytics_summary_cards(page):

    # ==========================
    # LOGIN
    # ==========================
    page.goto(LOGIN_URL)

    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    page.wait_for_timeout(5000)

    # ==========================
    # OPEN MODEL PAGE
    # ==========================
    dashboard = DashboardPage(page)

    dashboard.click_model_name()

    page.wait_for_timeout(5000)

    # ==========================
    # CLICK TAAS (LUY)
    # ==========================
    taas = page.locator("span.Noto").filter(has_text="TAAS")

    assert taas.count() > 0, "TAAS (LUY) model not found"

    taas.first.click(force=True)

    page.wait_for_timeout(5000)

    # ==========================
    # CLICK DOCUMENT ANALYTICS
    # ==========================
    analytics_card = page.locator(
        "p.card-title:has-text('Document Analytics')"
    )

    assert analytics_card.count() > 0, "Document Analytics card not found"

    analytics_card.first.click(force=True)

    page.wait_for_timeout(5000)

    # ==========================
    # VERIFY PAGE LOADED
    # ==========================
    assert page.locator(
        "span:has-text('Document volume over time')"
    ).is_visible(), "Document Analytics page not loaded"

    # ==========================
    # TOTAL DOCUMENTS CARD
    # ==========================
    total_card = page.locator(
        "p:has-text('Total documents')"
    )

    assert total_card.is_visible(), "Total Documents card not visible"

    total_value = total_card.locator(
        "xpath=following::span[1]"
    ).text_content()

    print("Total Documents:", total_value)

    # ==========================
    # DAILY AVERAGE CARD
    # ==========================
    daily_card = page.locator(
        "p:has-text('Daily average')"
    )

    assert daily_card.is_visible(), "Daily Average card not visible"

    daily_value = daily_card.locator(
        "xpath=following::span[1]"
    ).text_content()

    print("Daily Average:", daily_value)

    # ==========================
    # PEAK VOLUME CARD
    # ==========================
    peak_card = page.locator(
        "p:has-text('Peak volume')"
    )

    assert peak_card.is_visible(), "Peak Volume card not visible"

    peak_value = peak_card.locator(
        "xpath=following::span[1]"
    ).text_content()

    print("Peak Volume:", peak_value)

    # ==========================
    # LOWEST VOLUME CARD
    # ==========================
    lowest_card = page.locator(
        "p:has-text('Lowest volume')"
    )

    assert lowest_card.is_visible(), "Lowest Volume card not visible"

    lowest_value = lowest_card.locator(
        "xpath=following::span[1]"
    ).text_content()

    print("Lowest Volume:", lowest_value)

    # ==========================
    # VERIFY VALUES PRESENT
    # ==========================
    assert total_value.strip() != ""
    assert daily_value.strip() != ""
    assert peak_value.strip() != ""
    assert lowest_value.strip() != ""

    print("TC_49 PASSED")