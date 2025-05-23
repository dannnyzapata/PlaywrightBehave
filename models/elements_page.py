from playwright.async_api import Page, expect

from models.base_page import BasePage


class ElementsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.textBoxButton = page.get_by_role("list").get_by_text("Text Box")
        self.nameBox = page.get_by_role("textbox", name="Full Name")
        self.emailBox = page.get_by_role("textbox", name="name@example.com")
        self.addressCurrentBox = page.get_by_role("textbox", name="Current Address")
        self.addressNewBox = page.locator("#permanentAddress")
        self.submitButton = page.get_by_role("button", name="Submit")

    async def verify_text_box_page(self):
        await self.textBoxButton.is_visible()

    async def go_to_tex_box(self):
        await self.textBoxButton.click()

    async def fill_name(self, text):
        await self.nameBox.is_visible()
        await self.nameBox.fill(text)

    async def fill_email(self, text):
        await self.emailBox.is_visible()
        await self.emailBox.fill(text)

    async def fill_address_curr(self, text):
        await self.addressCurrentBox.is_visible()
        await self.addressCurrentBox.fill(text)

    async def fill_address_new(self, text):
        await self.addressNewBox.is_visible()
        await self.addressNewBox.fill(text)

    async def click_button(self):
        await self.submitButton.is_visible()
        await self.submitButton.click()