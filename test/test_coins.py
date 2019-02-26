from src.coins import is_valid_coin
from src.models.valid_coin import *


def test_is_valid_coin__should_return_false_when_weight_doesnt_match():
    #arrange
    invalid_weight_coin = {
        'weight': 99,
        'diameter': 21.21
    }
    #act
    actual = is_valid_coin(invalid_weight_coin)
    #assert
    assert actual is False


def test_is_valid_coin__should_return_false_when_diameter_doesnt_match():
    #arrange
    invalid_diameter_coin = {
        'weight': 5,
        'diameter': 99
    }
    #act
    actual = is_valid_coin(invalid_diameter_coin)
    #assert
    assert actual is False


def test_is_valid_coin__should_return_true_when_weight_matches():
    #arrange
    #act
    actual = is_valid_coin(Nickel)
    #assert
    assert actual is True


def test_is_valid_coin__should_return_true_for_dime():
    #arrange
    #act
    actual = is_valid_coin(Dime)
    #assert
    assert actual is True


def test_is_valid_coin__should_return_true_for_quarter():
    #arrange
    #act
    actual = is_valid_coin(Quarter)
    #assert
    assert actual is True


def test_is_valid_coin__should_return_true_for_dollar():
    #arrange
    #act
    actual = is_valid_coin(Dollar)
    #assert
    assert actual is True