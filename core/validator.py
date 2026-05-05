class Validator:

    @staticmethod
    def validate_cart_items(items, expected_items):
        assert len(items) > 0, "Cart is empty"

        for item in expected_items:
            assert item in items, f"{item} not found in cart"