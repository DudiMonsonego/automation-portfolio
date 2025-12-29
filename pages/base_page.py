class BasePage:
    def __init__(self, page):
        self.page = page

    def wait_for_element(self, selector):
        self.page.wait_for_selector(selector)