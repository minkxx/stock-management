from datetime import datetime
from management import database, collection, logger


def add_data(item_name, quantity):
    date = str(datetime.now().date())
    document = {
        "item_name":item_name,
        "quantity":quantity,
        "date_added": date
    }
    database.add_item(document=document, collection=collection)
    logger.info(f"Added {quantity} {item_name} to store.")

def update_data(item_name, quantity):
    database.update_item(item_name=item_name, )

def delete_data(item_name):
    database.delete_item(item_name=item_name, collection=collection)
    logger.info(f"Deleted {item_name} from database.")

def display_all_data():
    data = database.get_all_items(collection=collection)

    for obj in data:
        print(f"{obj['item_name']} {obj['quantity']}")

