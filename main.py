from uuid import uuid4
import json

class API1:

    def __init__(self):
        self._storage = {}


# with open('product_groups.json', 'w') as f:
#     json.dump(f, indent=4, sort_keys=True)

with open('product_groups.json') as f:
    data = json.load(f)

result = []
for p in data:
    result.append({
        "id": uuid4(),
        "name": p['name'],
        "parent_id": p['parent_id'],
        ## add ancestors(names of the parents)
    })

print(result)

# object_hook = group_by_division


# def group_by_division(group):
#     return (group['fullName'], group['divName'])
# Group  division
# groups_by_division = {}
# for i in range(len(data)):
#     group, division = data[i]
#     if division not in groups_by_division.keys():
#         groups_by_division[division] = []
#     groups_by_division[division].append(group)


# def get(self, obj_id: str):
#     """Get an object."""
#     return self._storage.get(obj_id)
#
#
# def create(self, data: dict):
#     """Store one new object."""
#     new_obj = {**data, "id": uuid4()}
#     self._storage[new_obj["id"]] = new_obj
#     return new_obj
