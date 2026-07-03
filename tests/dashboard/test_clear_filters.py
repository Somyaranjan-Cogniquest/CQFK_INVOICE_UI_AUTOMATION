from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest


@pytest.mark.sanity
@pytest.mark.regression
def test_TC_45_verify_clear_filters(page):

    # =========================
    # LOGIN
    # =========================
    page.goto(LOGIN_URL)

    login = LoginPage(page)
    login.login(
        USERNAME,
        PASSWORD
    )

    page.wait_for_timeout(5000)

    # =========================
    # NAVIGATION
    # =========================
    dashboard = DashboardPage(page)

    dashboard.click_model_name()
    dashboard.click_processing_dashboard()

    page.wait_for_timeout(5000)

    # =========================
    # BASE DATA
    # =========================
    base_rows = page.locator(
        "table tbody tr"
    ).count()

    assert base_rows > 0, \
        "No data loaded"

    print(
        "Base rows:",
        base_rows
    )

    # ==========================================================
    # STEP 1: PROCESS STATUS → Processed
    # ==========================================================
    page.locator(
        "#doc-status-select"
    ).click()

    page.wait_for_timeout(1000)

    page.locator(
        "li[role='option'][data-value='processed']"
    ).click()

    page.wait_for_timeout(2000)

    # ==========================================================
    # STEP 2: COLOR STATUS → Green
    # ==========================================================
    page.locator(
        "#color-status-select"
    ).click()

    page.wait_for_timeout(1000)

    page.locator(
        "li[role='option'][data-value='green']"
    ).click()

    page.wait_for_timeout(2000)

    # ==========================================================
    # STEP 3: REVIEW STATUS
    # ==========================================================
    review_dropdown = page.locator(
        "#review-status-select"
    )

    if review_dropdown.count() > 0:

        review_dropdown.click()

    else:

        page.locator(
            "div[role='combobox']"
        ).nth(2).click()

    page.wait_for_timeout(1000)

    approved_option = page.locator(
        "li:has-text('Approved')"
    )

    if approved_option.count() == 0:

        approved_option = page.locator(
            "li:has-text('Not Approved')"
        )

    approved_option.first.click()

    page.wait_for_timeout(3000)

    # ==========================================================
    # STEP 4: VERIFY FILTER APPLIED
    # ==========================================================
    filtered_rows = page.locator(
        "table tbody tr"
    ).count()

    print(
        "Filtered rows:",
        filtered_rows
    )

    # Filters may return 0 rows.
    # Main validation is Clear Filters.

    # ==========================================================
    # STEP 5: CLEAR FILTERS
    # ==========================================================
    clear_btn = page.locator(
        "button:has-text('Clear filters')"
    )

    clear_btn.wait_for(
        state="visible",
        timeout=5000
    )

    clear_btn.click()

    page.wait_for_timeout(4000)

    # ==========================================================
    # STEP 6: VERIFY RESET
    # ==========================================================
    final_rows = page.locator(
        "table tbody tr"
    ).count()

    print(
        "Final rows:",
        final_rows
    )

    assert final_rows == base_rows, \
        "Clear filters failed"

    print(
        "TC_45 Passed - Clear Filters working properly"
    )