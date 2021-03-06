from src.models.valid_coin import *


def is_valid_coin(coin):
    for valid_coin in valid_coins:
        if coin['weight'] == valid_coin['weight'] and coin['diameter'] == valid_coin['diameter']:
            return True
    return False



    # if coin['weight'] == Nickel['weight'] and coin['diameter'] == Nickel['diameter']:
    #     return True
    # elif coin['weight'] == Dime['weight'] and coin['diameter'] == Dime['diameter']:
    #     return True
    # elif coin['weight'] == Quarter['weight'] and coin['diameter'] == Quarter['diameter']:
    #     return True
    # elif coin['weight'] == Dollar['weight'] and coin['diameter'] == Dollar['diameter']:
    #     return True
    # else:
    #     return False


def count_change(coins):
    Total = 0
    for coin in coins:
        Total += coin['value']
    return Total

def return_change(count_change, product_cost):
    change_returned = []
    return_value = count_change - product_cost
    for coin in valid_coins:
        while coin['value'] <= round(return_value, 2):
            change_returned.append(coin)
            return_value = return_value - coin['value']
    return change_returned