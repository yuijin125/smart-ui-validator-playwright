import json
import os


class DataWriter:

    @staticmethod
    def save_products(products):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        file_path = os.path.join(base_dir, "data", "products.json")

        with open(file_path, "w") as f:
            json.dump(products, f, indent=4)