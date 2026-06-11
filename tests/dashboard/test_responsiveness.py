from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def test_TC_41_verify_responsiveness(page):

    # ==========================
    # LOGIN
    # ==========================
    page.goto(LOGIN_URL)

    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    page.wait_for_timeout(4000)

    # ==========================
    # NAVIGATION
    # ==========================
    dashboard = DashboardPage(page)

    dashboard.click_model_name()
    dashboard.click_processing_dashboard()

    page.wait_for_timeout(4000)

    # ==========================
    # RESPONSIVENESS TEST
    # ==========================
    viewports = [
        (1920, 1080),
        (1366, 768),
        (1024, 768),
        (768, 1024),
        (375, 667)
    ]

    for width, height in viewports:

        page.set_viewport_size({"width": width, "height": height})
        page.wait_for_timeout(2000)

        print(f"Checking UI responsiveness at {width}x{height}")

        # Table visibility
        assert page.locator("table").is_visible(), f"Table not visible at {width}x{height}"

        # Pagination dropdown
        assert page.locator("select.pgtotal").is_visible(), f"Pagination missing at {width}x{height}"

        # UI controls enabled
        assert page.locator("select.pgtotal").is_enabled(), f"UI broken at {width}x{height}"

        # Rows present
        rows = page.locator("table tbody tr")
        assert rows.count() > 0, f"No data at {width}x{height}"

    print("✅ TC_41 PASSED: UI is responsive across all screen sizes")