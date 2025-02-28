import pytest
from settings import Settings
from page_object_models.entry_page import EntryPage
from playwright.sync_api import expect

settings = Settings()

@pytest.fixture()
def setup_teardown(page):
    """
    This fixture uses page context and executes all the testcases on the same page.
    """
    entry_page = EntryPage(page)
    page.set_default_timeout(timeout=settings.DEFAULT_TIMEOUT)
    entry_page.navigate(settings.HOST)
    yield page
