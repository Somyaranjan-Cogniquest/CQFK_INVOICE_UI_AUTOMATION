from config.config import LOGIN_URL

def test_TC_07_password_mask(page):

    page.goto(LOGIN_URL)

    page.fill("#formBasicPassword", "Test123")

    password_type = page.locator("#formBasicPassword").get_attribute("type")

    assert password_type == "password", "Password is not masked"