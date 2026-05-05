import requests


class APIClient:

    BASE_URL = "https://dummyjson.com"

    @staticmethod
    def get_products():
        response = requests.get(f"{APIClient.BASE_URL}/products")

        assert response.status_code == 200, "API failed"

        return response.json()