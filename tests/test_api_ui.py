from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from core.api_client import APIClient


def test_ui_vs_api_products(setup):
    page = setup

    login = LoginPage(page)
    inventory = InventoryPage(page)

    # UI login
    login.login("standard_user", "secret_sauce")

    # UI data
    ui_products = inventory.get_all_product_names()

    print("UI Products:", ui_products)

    # API data
    api_data = APIClient.get_products()
    api_products = [p["title"] for p in api_data["products"]]

    print("API Products:", api_products)

    # Basic validations
    assert len(ui_products) > 0
    assert len(api_products) > 0