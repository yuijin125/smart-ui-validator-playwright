class BasePage:
    def __init__(self, page):
        self.page = page

    # click
    def click(self, locator):
        element = self.page.locator(locator)
        element.wait_for(state="visible")
        element.click()

    #fill
    def fill(self, locator, value):
        element = self.page.locator(locator)
        element.wait_for(state="visible")
        element.fill(value)

    def get_text(self, locator):
        return self.page.locator(locator).inner_text()