from src.services.products import Products


def purchase_product(product_location, coins):
    product = Products()
    if product.is_product_available(product_location) == False:
        return {'message': 'Product Not Available'}
