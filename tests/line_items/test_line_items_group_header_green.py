from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
import re

import pytest

@pytest.mark.smoke
@pytest.mark.regression
def test_TC_01_line_item_group_header_green(page):

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
            ).click(
                force=True
            )

            page.wait_for_timeout(2000)

            row.get_by_text(
                "View document"
            ).click(
                force=True
            )

            document_found = True

            break

    assert document_found, \
        "No 100% processed document found"

    print(
        "Document opened successfully"
    )

    # ==================================
    # STEP 4 : VERIFY DATA FIELD PAGE
    # ==================================

    assert page.locator(
        "input"
    ).count() > 0, \
        "Data Fields page not opened"

    print(
        "Data Fields page opened"
    )

    # ==================================
    # STEP 5 : OPEN LINE ITEMS PAGE
    # ==================================

    line_items_tab = page.locator(
        "span:has-text('Line Items')"
    ).filter(
        has_not_text="Data Field"
    ).first

    print(
        "Line Items Tab Count =",
        line_items_tab.count()
    )

    line_items_tab.evaluate(
        "(element) => element.click()"
    )

    page.wait_for_timeout(3000)

    print(
        "Clicked Line Items Tab"
    )

    # ==================================
    # STEP 6 : FETCH COUNTS
    # ==================================

    badges = page.locator(
        "span[style*='inline-flex']"
    )

    texts = []

    for i in range(badges.count()):

        text = badges.nth(i).inner_text().strip()

        if text:

            texts.append(text)

    print("Badge Texts :", texts)

    # Last 4 values belong to Line Items

    all_count = int(
        texts[-4]
        .replace("All", "")
        .strip()
    )

    green_count = int(texts[-3])

    red_count = int(texts[-2])

    gray_count = int(texts[-1])

    print(
        f"All Count : {all_count}"
    )

    print(
        f"Green Count : {green_count}"
    )

    print(
        f"Red Count : {red_count}"
    )

    print(
        f"Gray Count : {gray_count}"
    )

    # ==================================
    # STEP 7 : VALIDATE COUNTS
    # ==================================

    assert (
        green_count +
        red_count +
        gray_count
    ) == all_count, \
        (
            f"Count mismatch : "
            f"All={all_count}, "
            f"Green={green_count}, "
            f"Red={red_count}, "
            f"Gray={gray_count}"
        )

    print(
        "Count validation successful"
    )

    # ==================================
    # STEP 8 : VALIDATE ALL GREEN
    # ==================================

    assert green_count == all_count, \
        (
            f"Expected all line items green. "
            f"Green={green_count}, "
            f"All={all_count}"
        )

    assert red_count == 0, \
        (
            f"Red Count should be 0 "
            f"but found {red_count}"
        )

    assert gray_count == 0, \
        (
            f"Gray Count should be 0 "
            f"but found {gray_count}"
        )

    print(
        "PASS : All Line Items are Green"
    )