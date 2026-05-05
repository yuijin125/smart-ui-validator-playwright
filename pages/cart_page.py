from pages.base_page import BasePage


class CartPage(BasePage):

    CART_ITEMS = ".inventory_item_name"

    def get_cart_items(self):
        return self.page.locator(self.CART_ITEMS).all_inner_texts()

    # existing generic remove
    def remove_item(self):
        self.page.locator("button[data-test^='remove']").first.click()

    # Removing_specific_product
    def remove_product_by_name(self, product_name):
        item = self.page.locator(".cart_item").filter(has_text=product_name)
        item.locator("button[data-test^='remove']").click()