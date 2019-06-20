import json


def get_product_by_location(product_location):
    with open('C:/Users/kdoebel36/PycharmProjects/vending_machine/inventory.json', 'r') as inventory:
        inventory1 = json.load(inventory)
    for product in inventory1:
        if product['location'] == product_location:
            return product
