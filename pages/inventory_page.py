class InventoryPage:

    PRODUCT_NAMES = ".inventory_item_name"
    ADD_TO_CART_BTN = "button[data-test^='add-to-cart']"
    CART_ICON = ".shopping_cart_link"

    def __init__(self, page):
        self.page = page

    def get_all_product_names(self):
        return self.page.locator(self.PRODUCT_NAMES).all_inner_texts()

    def add_first_product_to_cart(self):
        self.page.locator(self.ADD_TO_CART_BTN).first.click()

    def add_multiple_products(self, count):
        buttons = self.page.locator(self.ADD_TO_CART_BTN)
        for i in range(count):
            buttons.nth(i).click()

    def add_product_by_name(self, product_name):
        item = self.page.locator(".inventory_item").filter(has_text=product_name)
        item.locator(self.ADD_TO_CART_BTN).click()

    def go_to_cart(self):
        self.page.click(self.CART_ICON)

    def get_cart_count(self):
        badge = self.page.locator(".shopping_cart_badge")
        return badge.inner_text() if badge.count() > 0 else "0"

    # 🔥 THIS WAS REMOVED — REQUIRED
    def get_products_with_prices(self):
        names = self.page.locator(".inventory_item_name").all_inner_texts()
        prices = self.page.locator(".inventory_item_price").all_inner_texts()

        products = []

        for i in range(len(names)):
            products.append({
                "name": names[i],
                "price": prices[i]
            })

        return products