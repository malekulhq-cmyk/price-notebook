import json
import os

FILE = "items.json"


def load_data():
    if not os.path.exists(FILE):
        return []

    try:
        with open(FILE, "r") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        return []


def save_data(items):
    with open(FILE, "w") as file:
        json.dump(items, file, indent=4)


def add_item(items, item, price):
    items.append({
        "item": item,
        "price": price
    })

    save_data(items)


def delete_item(items, item_name):
    for i, data in enumerate(items):

        if data["item"].lower() == item_name.lower():

            deleted = items.pop(i)

            save_data(items)

            return deleted

    return None


def update_price(items, item_name, new_price):

    for data in items:

        if data["item"].lower() == item_name.lower():

            old_price = data["price"]

            data["price"] = new_price

            save_data(items)

            return old_price

    return None