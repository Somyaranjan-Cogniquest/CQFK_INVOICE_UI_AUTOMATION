import pytest
import os
import allure
from playwright.sync_api import sync_playwright
from pytest_metadata.plugin import metadata_key

from config.config import LOGIN_URL
from test_data.test_data import USERNAME, PASSWORD


# ==========================================================
# PYTEST CONFIGURE
# ==========================================================
def pytest_configure(config):

    # HTML Report Metadata
    config.stash[metadata_key]["Application"] = "CQFK Invoice "
    config.stash[metadata_key]["Application URL"] = (
        "https://gpucontainer.cogniquest.ai/InvIDPApi"
    )
    config.stash[metadata_key]["Application Version"] = "v1.6"
    config.stash[metadata_key]["Executed By"] = "Somyaranjan Sahoo"
    config.stash[metadata_key]["Framework"] = "Pytest + Playwright"
    config.stash[metadata_key]["Browser"] = "Chromium"
   

    # Remove unwanted metadata
    config.stash[metadata_key].pop(
        "JAVA_HOME",
        None
    )

    config.stash[metadata_key].pop(
        "Packages",
        None
    )

    # ==========================================
    # Create Allure Environment Information
    # ==========================================
    os.makedirs(
        "allure-results",
        exist_ok=True
    )

    with open(
        "allure-results/environment.properties",
        "w"
    ) as f:

        f.write(
            "Application=CQFK Invoice UI\n"
            "Environment=GPU Container\n"
            "Application URL=https://gpucontainer.cogniquest.ai/InvIDPApi\n"
            "Version=v1.6\n"
            "Executed By=Somyaranjan Sahoo\n"
            "Framework=Pytest + Playwright\n"
            "Browser=Chromium\n"
        )


# ==========================================================
# HTML REPORT TITLE
# ==========================================================
def pytest_html_report_title(report):

    report.title = (
        "CQFK Invoice UI Automation Report - "
        "GPU Container v1.6"
    )




# ==========================================================
# PAGE FIXTURE
# ==========================================================
@pytest.fixture
def page(request):

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False,
            args=[
                "--start-maximized",
                "--force-device-scale-factor=1"
            ]
        )

        context = browser.new_context(
            no_viewport=True
        )

        page = context.new_page()

        yield page

        # ==========================================
        # Screenshot on Failure
        # ==========================================
        if (
            hasattr(request.node, "rep_call")
            and request.node.rep_call.failed
        ):

            os.makedirs(
                "screenshots",
                exist_ok=True
            )

            screenshot_path = (
                f"screenshots/"
                f"{request.node.name}.png"
            )

            page.screenshot(
                path=screenshot_path,
                full_page=True
            )

            # Attach screenshot to Allure
            allure.attach.file(
                screenshot_path,
                name="Failure Screenshot",
                attachment_type=
                allure.attachment_type.PNG
            )

            print(
                f"\nScreenshot saved : "
                f"{screenshot_path}"
            )

        context.close()
        browser.close()


# ==========================================================
# STORE TEST RESULT
# ==========================================================
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(
        item,
        call
):

    outcome = yield
    rep = outcome.get_result()

    setattr(
        item,
        "rep_" + rep.when,
        rep
    )


# ==========================================================
# LOGIN FIXTURE
# ==========================================================
@pytest.fixture
def login(page):

    page.goto(LOGIN_URL)

    page.wait_for_timeout(2000)

    page.fill(
        "input[type='text']",
        USERNAME
    )

    page.fill(
        "input[type='password']",
        PASSWORD
    )

    page.click(
        "button"
    )

    page.wait_for_timeout(3000)

    return page