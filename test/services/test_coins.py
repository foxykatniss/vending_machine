from src.services.coins import *
from src.models.valid_coin import *


def test_is_valid_coin__should_return_false_when_weight_doesnt_match():
    # arrange
    invalid_weight_coin = {
        'weight': 99,
        'diameter': 21.21
    }
    # act
    actual = is_valid_coin(invalid_weight_coin)
    # assert
    assert actual is False


def test_is_valid_coin__should_return_false_when_diameter_doesnt_match():
    # arrange
    invalid_diameter_coin = {
        'weight': 5,
        'diameter': 99
    }
    # act
    actual = is_valid_coin(invalid_diameter_coin)
    # assert
    assert actual is False


def test_is_valid_coin__should_return_true_when_weight_matches():
    # arrange
    # act
    actual = is_valid_coin(Nickel)
    # assert
    assert actual is True


def test_is_valid_coin__should_return_true_for_dime():
    # arrange
    # act
    actual = is_valid_coin(Dime)
    # assert
    assert actual is True


def test_is_valid_coin__should_return_true_for_quarter():
    # arrange
    # act
    actual = is_valid_coin(Quarter)
    # assert
    assert actual is True


def test_is_valid_coin__should_return_true_for_dollar():
    # arrange
    # act
    actual = is_valid_coin(Dollar)
    # assert
    assert actual is True


def test_is_count_change__should_return_value_for_single_coin():
    # arrange
    # act
    actual = count_change([Quarter])
    # assert
    assert actual == 0.25


def test_is_count_change__should_return_nickel_value():
    # arrange
    # act
    actual = count_change([Nickel])
    # assert
    assert actual == 0.05


def test_is_count_change__should_return_dime_value():
    # arrange
    # act
    actual = count_change([Dime])
    # assert
    assert actual == 0.1


def test_is_count_change__should_return_dollar_value():
    # arrange
    # act
    actual = count_change([Dollar])
    # assert
    assert actual == 1.0


def test_is_count_change__should_return_value_for_multiples():
    # arrange
    # act
    coins_list = [Quarter, Dime]
    actual = count_change(coins_list)
    # assert
    assert actual == 0.35


def test_count_change__should_count_empty_list():
    # arrange
    # act
    coins_list = []
    actual = count_change(coins_list)
    # assert
    assert actual == 0

def test_return_change__should_return_single_coin():
    #arrange
    count_change = 0.25
    product_cost = 0.15
    actual = return_change(count_change, product_cost)
    assert actual == [Dime]

def test_return_change__should_return_mult_coins():
    count_change = 0.50
    product_cost = 0.35
    actual = return_change(count_change, product_cost)
    assert actual == [Dime, Nickel]


def test_return_change__should_round_coin_values():
    count_change = 0.70
    product_cost = 0.35
    actual = return_change(count_change, product_cost)
    assert actual == [Quarter, Dime]

def test_return_change__should_mult_single_coins():
    count_change = 1.00
    product_cost = 0.50
    actual = return_change(count_change, product_cost)
    assert actual == [Quarter, Quarter]