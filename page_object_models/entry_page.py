from playwright.sync_api import Page

class EntryPage:
    def __init__(self, page: Page):
        self.page = page
        self.login_btn = page.locator("(//button[span='Login'])[2]")
        self.register_btn = page.locator("(//button[span='Register'])[2]")
        self.username = page.get_by_label('Email')
        self.password = page.get_by_label("Password")
        self.submit_login_creds = page.locator("//form/button[span=' Login ']")
        self.submit_registration_creds = page.locator("//form/button[span=' Register ']")
        self.home_btn = page.locator("//button[span='Home']")
        self.sign_out_btn = page.locator('//span[text()="Sign Out"]')
        
    def navigate(self, link: str) -> None:
        """
        This method navigates user to any give site.
        :param link:
        :return:
        """
        self.page.goto(link)

    def register(self, username: str, password: str) -> None:
        """
        This method performs registration to platform.
        :param username:
        :param password:
        :return:
        """
        self.register_btn.click()
        self.username.fill(username)
        self.password.fill(password)
        self.submit_registration_creds.click()
        self.page.get_by_text("Registration Successful!").wait_for(state="visible")

    def login(self, username: str, password: str) -> None:
        """
        This method performs login to platform.
        :param username:
        :param password:
        :return:
        """
        self.home_btn.click()
        self.login_btn.click()
        self.username.fill(username)
        self.password.fill(password)
        self.submit_login_creds.click()
        self.page.locator('//span[text()="Create Support Ticket"]').wait_for(state="visible")        

    def logout(self) -> None: 
        """
        This method logouts user from platform.
        :return:
        """
        try:
            self.sign_out_btn.click()
        except Exception as e:
            pass    