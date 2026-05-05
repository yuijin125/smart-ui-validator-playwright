from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from core.validator import Validator
from core.data_loader import DataLoader

data = DataLoader.load_test_data()


def test_add_product_to_cart(setup):
    page = setup

    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)

    creds = data["login"]["valid"]
    product = data["products"]["single"]

    login.login(creds["username"], creds["password"])

    inventory.add_product_by_name(product)

    assert inventory.get_cart_count() == "1"

    inventory.go_to_cart()

    items = cart.get_cart_items()

    Validator.validate_cart_items(items, [product])