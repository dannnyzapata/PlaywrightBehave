from playwright.async_api import Page, expect

from models.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.welcomeMessage = page.get_by_role("link", name="Selenium Online Training")
        self.elementsButton = page.get_by_role("heading", name="Elements")

    async def navigate(self):
        await self.page.goto("https://demoqa.com/", timeout=5000)

    async def verify_main_page(self):
        await self.welcomeMessage.is_visible()

    async def click_elements(self):
        await self.elementsButton.click()
