from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_TC_97_verify_status_counts_match_total(page):

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
    # STEP 2 : OPEN MODEL
    # ==================================
    dashboard = DashboardPage(page)

    dashboard.click_model_name()

    print("Model Landing Page Opened")

    # ==================================
    # STEP 3 : OPEN PROCESSING DASHBOARD
    # ==================================
    dashboard.click_processing_dashboard()

    dashboard.wait_for_table()

    print("Processing Dashboard Opened")

    # ==================================
    # STEP 4 : OPEN FIRST 100% DOCUMENT
    # ==================================
    rows = page.locator(
        "table tbody tr"
    )

    total_rows = rows.count()

    document_opened = False

    for i in range(total_rows):

        row = rows.nth(i)

        if "100%" in row.inner_text():

            menu_button = row.locator(
                "button.dropdown-toggle"
            )

            menu_button.first.click(
                force=True
            )

            page.wait_for_timeout(2000)

            view_document = row.locator(
                "a[title='View Document']"
            )

            if view_document.count() > 0:

                view_document.first.click(
                    force=True
                )

                document_opened = True

                break

    assert document_opened, \
        "No 100% processed document found"

    print("Data Field Page Opened")

    # ==================================
    # STEP 5 : GET COUNT VALUES
    # ==================================
    count_spans = page.locator(
        "span"
    )

    count_values = []

    for i in range(count_spans.count()):

        try:

            value = count_spans.nth(i).inner_text().strip()

            if value.isdigit():

                count_values.append(
                    int(value)
                )

        except Exception:
            continue

    print(
        "Numeric Counts Found :",
        count_values
    )

    assert len(count_values) >= 4, \
        "Unable to find Total, Green, Red and Gray counts"

    # Example:
    # [23,20,2,1]

    total_count = count_values[0]

    green_count = count_values[1]

    red_count = count_values[2]

    gray_count = count_values[3]

    print(
        f"Total Count : {total_count}"
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
    # STEP 6 : VALIDATE COUNTS
    # ==================================
    calculated_total = (
        green_count +
        red_count +
        gray_count
    )

    print(
        f"{green_count} + {red_count} + {gray_count} = {calculated_total}"
    )

    assert calculated_total == total_count, \
        "Green + Red + Gray count does not match Total count"

    print(
        "PASS : Green + Red + Gray count equals Total count"
    )