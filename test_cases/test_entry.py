import pytest
from playwright.sync_api import Page, expect
from page_object_models.entry_page import EntryPage
import faker
import os
from settings import Settings

settings = Settings()
f = faker.Faker()
os.environ['PLAYWRIGHT_EXP_APP_USERNAME'] = f.email()

@pytest.mark.order(1)
def test_registration(setup_teardown: Page, browser_name):
    if browser_name == 'webkit' or browser_name == 'firefox':
        os.environ['PLAYWRIGHT_EXP_APP_USERNAME'] = f.email() # handling re-registration on new browser
    page = setup_teardown
    entry_page = EntryPage(page)
    entry_page.register(os.getenv('PLAYWRIGHT_EXP_APP_USERNAME'), settings.HOST_PASSWORD)    
    expect(page.get_by_text("Registration Successful!")).to_be_visible()
    entry_page.login(os.getenv('PLAYWRIGHT_EXP_APP_USERNAME'), settings.HOST_PASSWORD)
    expect(page.locator("//span[text()='Create Support Ticket']")).to_be_visible()
    entry_page.logout()