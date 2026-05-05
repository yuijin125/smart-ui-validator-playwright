from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from core.data_writer import DataWriter


def test_extract_products(setup):
    page = setup

    login = LoginPage(page)
    inventory = InventoryPage(page)

    login.login("standard_user", "secret_sauce")

    products = inventory.get_products_with_prices()

    print(products)

    DataWriter.save_products(products)

    assert len(products) > 0