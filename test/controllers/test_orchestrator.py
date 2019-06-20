from src.controllers.orchestrator import purchase_product


def test_purchase_product__should_return_not_available():
    product_location = 'G6'
    coins = []
    purchase = purchase_product(product_location, coins)
    assert purchase['message'] == 'Product Not Available'