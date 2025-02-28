import pytest
from playwright.sync_api import Page, expect
from page_object_models.entry_page import EntryPage
from page_object_models.create_action import Create
import faker
import os
from random import randrange
from settings import Settings

settings = Settings()
f = faker.Faker()
title = f.sentence(nb_words=randrange(1,4))
desc = f.paragraph(nb_sentences=randrange(1,5))


@pytest.mark.order(3)
def test_support_ticket_creation(setup_teardown: Page):
    '''
    This test logs into the platform creates a ticket and asserts the ticket creation
    '''
    page = setup_teardown
    entry_page = EntryPage(page)
    create = Create(page)
    entry_page.login(os.getenv('PLAYWRIGHT_EXP_APP_USERNAME'), settings.HOST_PASSWORD)
    create.support_ticket(title, desc)
    expect(page.get_by_text("Ticket created Successfully!")).to_be_visible()
    entry_page.logout()

@pytest.mark.parametrize("case_name", [(title)]) # implemented parameterization here just for demo
@pytest.mark.order(4)
def test_case_creation(setup_teardown: Page, case_name: str):
    '''
    This test logs into the platform creates a case and asserts the case creation
    :param case_name:
    '''
    page = setup_teardown
    entry_page = EntryPage(page)
    create = Create(page)
    entry_page.login(os.getenv('PLAYWRIGHT_EXP_APP_USERNAME'), settings.HOST_PASSWORD)
    create.case(case_name)
    expect(page.get_by_text("Case created Successfully!")).to_be_visible()
    entry_page.logout()
