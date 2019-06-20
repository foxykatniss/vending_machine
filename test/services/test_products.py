from mock import patch

from src.services.products import *


def test_is_sufficient_funds__should_return_false_if_insufficient():
    # arrange
    product_cost = 1.00
    amount_inserted = 0.75
    # act
    actual = is_sufficient_funds(product_cost, amount_inserted)
    # assert
    assert actual == False


def test_is_sufficient_funds__should_return_true_if_greater():
    product_cost = 1.00
    amount_inserted = 1.75
    actual = is_sufficient_funds(product_cost, amount_inserted)
    assert actual == True


def test_is_sufficient_funds__should_return_true_if_equal():
    product_cost = 1.00
    amount_inserted = 1.00
    actual = is_sufficient_funds(product_cost, amount_inserted)
    assert actual == True

@patch('src.services.products.get_product_by_location')
def test_get_product_cost__should_return_cost(mock_inventory):
    # arrange
    product_location = 'A2'
    mock_inventory.return_value = [{'location': product_location, 'cost': 1.00}]
    products = Products()
    # act
    actual = products.get_product_cost(product_location)
    # assert
    assert actual == 1.00

@patch('src.services.products.get_product_by_location')
def test_get_product_cost__should_return_0(mock_inventory):
    # arrange
    mock_inventory.return_value = []
    product_location = 'B2'
    products = Products()
    # act
    actual = products.get_product_cost(product_location)
    # assert
    assert actual == 0


@patch('src.services.products.get_product_by_location')
def test_is_product_available__should_return_False_when_database_empty(mock_inventory):
    product_location = 'G2'
    mock_inventory.return_value = []
    product = Products()

    actual =product.is_product_available(product_location)

    assert actual == False

@patch('src.services.products.get_product_by_location')
def test_is_product_available__should_return_True_when_database_has_value(mock_inventory):
    product_location = 'A2'
    mock_inventory.return_value = [{'item': 'Funions', 'cost': 1.00}]
    product = Products()

    actual = product.is_product_available(product_location)
    assert actual == True

def test_get_product_cost__shouldnt_query_database_when_result_cached():
    product_location = 'A2'
    product = Products()
    product.current_product = [{'item': 'Funions', 'cost': 1.00}]
    actual = product.get_product_cost(product_location)

    assert actual == 1.00