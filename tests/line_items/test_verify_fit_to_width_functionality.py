from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
import re

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_TC_fit_to_width_functionality(page):

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

            print(
                f"100% document found in row {i + 1}"
            )

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
    # STEP 5 : GET DEFAULT ZOOM
    # ==================================
    zoom_label = page.locator(
        "span"
    ).filter(
        has_text="%"
    ).first

    default_zoom_text = zoom_label.inner_text()

    default_zoom = int(
        re.findall(
            r"\d+",
            default_zoom_text
        )[0]
    )

    print(
        f"Default Zoom = {default_zoom}%"
    )

    # ==================================
    # STEP 6 : CLICK ZOOM IN
    # ==================================
    zoom_in_button = page.locator(
        "button:has(svg g#Square_Plus)"
    ).first

    zoom_in_button.click()

    page.wait_for_timeout(3000)

    zoom_after_in_text = zoom_label.inner_text()

    zoom_after_in = int(
        re.findall(
            r"\d+",
            zoom_after_in_text
        )[0]
    )

    print(
        f"Zoom After Zoom-In = {zoom_after_in}%"
    )

    assert zoom_after_in > default_zoom, \
        "Zoom In did not increase zoom level"

    # ==================================
    # STEP 7 : CLICK FIT TO WIDTH
    # ==================================
    fit_width_button = page.locator(
        "button:has(img[alt='zoom'])"
    ).first

    fit_width_button.click()

    page.wait_for_timeout(3000)

    print("Fit To Width clicked")

    # ==================================
    # STEP 8 : VERIFY RESET
    # ==================================
    zoom_after_fit_text = zoom_label.inner_text()

    zoom_after_fit = int(
        re.findall(
            r"\d+",
            zoom_after_fit_text
        )[0]
    )

    print(
        f"Zoom After Fit Width = {zoom_after_fit}%"
    )

    assert zoom_after_fit < zoom_after_in, \
        "Fit To Width did not reduce zoom"

    print(
        "PASS : Fit To Width restored document view"
    )