from locators.login_locators import LoginLocators

class LoginPage:

    def __init__(self, page):
        self.page = page

    def enter_username(self, username):
        self.page.fill(LoginLocators.USERNAME, username)

    def enter_password(self, password):
        self.page.fill(LoginLocators.PASSWORD, password)

    def click_login(self):
        self.page.click(LoginLocators.LOGIN_BUTTON)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()