class InventoryPage:
    def __init__(self, page):
        self.page = page
        self._header = page.locator(".title")
        self._first_item_add_btn = page.locator("[data-test^='add-to-cart']").first
        self._cart_badge = page.locator(".shopping_cart_badge")
        self._cart_link = page.locator(".shopping_cart_link")

    def add_first_item_to_cart(self):
        self._first_item_add_btn.click()

    def get_cart_count(self):
        return self._cart_badge.text_content()

    def go_to_cart(self):
        self._cart_link.click()