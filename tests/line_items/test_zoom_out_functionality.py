from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
import re

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_TC_16_zoom_out_functionality(page):

    # ==================================
    # STEP 1 : LOGIN
    # ==================================
    page.goto(LOGIN_URL)

    login = LoginPage(page)

    login.login(
        USERNAME,
        PASSWORD
    )

    # ==================================
    # STEP 2 : OPEN PROCESSING DASHBOARD
    # ==================================
    dashboard = DashboardPage(page)

    dashboard.click_model_name()

    dashboard.click_processing_dashboard()

    dashboard.wait_for_table()

    print("Processing Dashboard opened")

    # ==================================
    # STEP 3 : OPEN FIRST 100% DOCUMENT
    # ==================================
    rows = page.locator(
        "table tbody tr"
    )

    document_found = False

    for i in range(rows.count()):

        row = rows.nth(i)

        if "100%" in row.inner_text():

            row.locator(
                "button.dropdown-toggle"
            ).click(force=True)

            page.wait_for_timeout(2000)

            row.get_by_text(
                "View document"
            ).click(force=True)

            document_found = True

            break

    assert document_found, \
        "No 100% processed document found"

    print("Document opened successfully")

    # ==================================
    # STEP 4 : OPEN LINE ITEMS TAB
    # ==================================
    line_items_tab = page.locator(
        "span:has-text('Line Items')"
    ).first

    line_items_tab.click()

    page.wait_for_timeout(3000)

    print("Line Items tab opened")

    # ==================================
    # STEP 5 : GET CURRENT ZOOM %
    # ==================================
    zoom_label = page.locator(
        "span"
    ).filter(
        has_text="%"
    ).first

    before_zoom_text = zoom_label.inner_text()

    before_zoom = int(
        re.findall(
            r"\d+",
            before_zoom_text
        )[0]
    )

    print(
        f"Zoom Before = {before_zoom}%"
    )

    # ==================================
    # STEP 6 : CLICK ZOOM OUT (-)
    # ==================================
    zoom_out_button = page.locator(
        "button:has(svg g#Square_Minus)"
    ).first

    zoom_out_button.click()

    print("Zoom Out button clicked")

    page.wait_for_timeout(3000)

    # ==================================
    # STEP 7 : GET UPDATED ZOOM %
    # ==================================
    zoom_updated = False

    for _ in range(10):

        try:

            zoom_text = page.locator(
                "span"
            ).filter(
                has_text="%"
            ).first.inner_text()

            after_zoom = int(
                re.findall(
                    r"\d+",
                    zoom_text
                )[0]
            )

            if after_zoom < before_zoom:

                zoom_updated = True

                break

        except Exception:
            pass

        page.wait_for_timeout(1000)

    assert zoom_updated, \
        "Zoom percentage did not decrease"

    print(
        f"Zoom After = {after_zoom}%"
    )

    # ==================================
    # STEP 8 : VALIDATE
    # ==================================
    assert after_zoom < before_zoom, \
        (
            f"Zoom did not decrease. "
            f"Before={before_zoom}% "
            f"After={after_zoom}%"
        )

    print(
        "PASS : PDF zoom level decreased successfully"
    )