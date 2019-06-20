from src.Database.Inventory import get_product_by_location


class Products:
    current_product = None

    def get_product_cost(self, product_location):
        if self.current_product == None:
            for product in get_product_by_location(product_location):
                if product_location == product['location']:
                    return product['cost']
            return 0
        first_prod = self.current_product[0]
        return first_prod['cost']

    def is_product_available(self, product_location):
        self.current_product = get_product_by_location(product_location)
        if self.current_product == None:
            return False
        return True


def is_sufficient_funds(product_cost, amount_inserted):
    if product_cost <= amount_inserted:
        return True
    return False
