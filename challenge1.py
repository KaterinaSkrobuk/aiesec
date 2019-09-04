from uuid import uuid4
import json


class API1:

    def __init__(self):
        self._storage = {}

# Loading the json Data
with open('test.json') as f:
    rawData = json.load(f)

# Formatting the data for easy access
data = {}
for product in rawData:
    data[product['id']] = product

# Loop through all the products
for key, product in data.items():
    parentID = product["parent_id"]

    ancestors = []

    if parentID:
        ancestors.append(data[parentID]['name'])

    while parentID:
        parentProduct = data[parentID]
        if not parentProduct['parent_id']:
            break
        parentID = parentProduct['parent_id']
        ancestors.append(data[parentID]['name'])

    newProduct = {
        "id": uuid4(),
        "name": product['name'],
        "parent_id": product['parent_id'],
        "ancestors": ancestors
    }




