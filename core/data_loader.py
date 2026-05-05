import json
import os


class DataLoader:

    @staticmethod
    def load_test_data():
        base_dir = os.path.dirname(os.path.dirname(__file__))
        file_path = os.path.join(base_dir, "data", "test_data.json")

        with open(file_path, "r") as f:
            return json.load(f)

    @staticmethod
    def load_products():
        base_dir = os.path.dirname(os.path.dirname(__file__))
        file_path = os.path.join(base_dir, "data", "products.json")

        with open(file_path, "r") as f:
            return json.load(f)