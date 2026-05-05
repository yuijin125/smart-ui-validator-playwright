from pages.login_page import LoginPage
from core.data_loader import DataLoader


data = DataLoader.load_test_data()


def test_valid_login(setup):
    page = setup
    login = LoginPage(page)

    creds = data["login"]["valid"]

    login.login(creds["username"], creds["password"])

    assert "inventory" in page.url


def test_invalid_login(setup):
    page = setup
    login = LoginPage(page)

    creds = data["login"]["invalid"]

    login.login(creds["username"], creds["password"])

    assert "Epic sadface" in login.get_error_message()