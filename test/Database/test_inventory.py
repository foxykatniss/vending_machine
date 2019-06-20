from src.Database.Inventory import get_product_by_location


def test_get_product_by_location__should_return_name():
    #arrange
    product_location = 'A1'
    #act
    actual = get_product_by_location(product_location)
    #assert
    assert actual['item'] == 'Snickers'


def test_get_product_by_location__should_return_cost():
    #arrange
    product_location = 'B2'
    #act
    actual = get_product_by_location(product_location)
    #assert
    assert actual['cost'] == 0.75
