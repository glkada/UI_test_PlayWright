from playwright.sync_api import Page


class Create:
    def __init__(self, page: Page):
        self.page = page
        self.create_ticket_btn = page.get_by_text("Create Support Ticket")
        self.create_case_btn = page.get_by_text("Create Case")
        self.ticket_title = page.locator("//div[label='Title']/input")
        self.ticket_description = page.locator("//div[label='Description']/textarea")
        self.ticket_submit_btn = page.locator("//button[span=' Submit Ticket ']")
        self.case_name = page.locator("//div[label='Case Name']/input")
        self.drop_down = page.get_by_role("combobox").locator("div").filter(has_text="Select ItemSelect Item").locator("div")
        self.select_option = self.page.get_by_role("option").nth(1) # have hard coded this since the drop down does not render as expected
        self.case_submit_btn = self.page.get_by_text(" Submit Case ")
        
    def support_ticket(self, title: str, desc: str) -> None:
        """
        This method creates a support ticket.
        :param title:
        :param desc:
        """
        self.create_ticket_btn.click()
        self.ticket_title.fill(title)
        self.ticket_description.fill(desc)
        self.ticket_submit_btn.click()

    def case(self, case_name: str) -> None:
        """
        This method creates a case.
        :param case name:
        """
        self.create_case_btn.click()
        self.case_name.fill(case_name)
        self.drop_down.click()
        self.select_option.click()
        self.case_submit_btn.click()
 