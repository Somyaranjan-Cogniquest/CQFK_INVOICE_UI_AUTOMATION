from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def test_TC_39_pagination(page):

    # Login
    page.goto(LOGIN_URL)

    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    page.wait_for_timeout(4000)

    dashboard = DashboardPage(page)

    # Navigate to Processing Dashboard
    dashboard.click_model_name()
    dashboard.click_processing_dashboard()

    page.wait_for_timeout(4000)

    # ==========================
    # STEP 1: Get initial row count
    # ==========================
    rows = page.locator("table tbody tr")
    initial_count = rows.count()

    assert initial_count > 0, "No rows found initially"

    print("Initial rows:", initial_count)

    # ==========================
    # STEP 2: Change Per Page = 20
    # ==========================
    page.locator("select.pgtotal").select_option("20")

    page.wait_for_timeout(3000)

    count_20 = page.locator("table tbody tr").count()

    print("Rows after selecting 20:", count_20)

    assert count_20 <= 20, "Per page 20 not working"

    # ==========================
    # STEP 3: Change Per Page = 10
    # ==========================
    page.locator("select.pgtotal").select_option("10")

    page.wait_for_timeout(3000)

    count_10 = page.locator("table tbody tr").count()

    print("Rows after selecting 10:", count_10)

    assert count_10 <= 10, "Per page 10 not working"

    # ==========================
    # STEP 4: Change Per Page = 30
    # ==========================
    page.locator("select.pgtotal").select_option("30")

    page.wait_for_timeout(3000)

    count_30 = page.locator("table tbody tr").count()

    print("Rows after selecting 30:", count_30)

    assert count_30 <= 30, "Per page 30 not working"

    # ==========================
    # STEP 5: Change Per Page = 40
    # ==========================
    page.locator("select.pgtotal").select_option("40")

    page.wait_for_timeout(3000)

    count_40 = page.locator("table tbody tr").count()

    print("Rows after selecting 40:", count_40)

    assert count_40 <= 40, "Per page 40 not working"

    print("✅ TC_39 PASSED: Pagination working correctly for all page sizes")