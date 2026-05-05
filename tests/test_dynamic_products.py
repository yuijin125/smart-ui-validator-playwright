import pytest
from core.data_loader import DataLoader
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

products = DataLoader.load_products()


@pytest.mark.parametrize("product", products)
def test_add_each_product(setup, product):
    page = setup

    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)

    login.login("standard_user", "secret_sauce")

    inventory.add_product_by_name(product["name"])
    inventory.go_to_cart()

    items = cart.get_cart_items()

    assert product["name"] in items