import json
from pathlib import Path
from models import Create

DATA_FILE = Path("grews.json")

def load_data():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding='UTF8') as f:
            return json.load(f)
    return {"": []}

def save_data(data):
    with open(DATA_FILE, "w", encoding='UTF8') as f:
        json.dump(data, f)

def get_data():
    data = load_data()
    return data

def create_data(create_data: Create):
    data = load_data()
    grew_id = len(data) + 1
    data.append({"id": grew_id, "name": create_data.name, "note": create_data.note})
    save_data(data)
    return grew_id

# def create_map(data: Update):
#     return {int(item["id"]): item for item in data}

# def update_data(update_data: Update):
#     data = load_data()
#     id_map = create_map(data)
    
#     if update_data.id in id_map.keys():
#         if update_data.name is not None:
#             id_map[update_data.id]['name'] = update_data.name
#         if update_data.note is not None:
#             id_map[update_data.id]['note'] = update_data.note

#         data = list(id_map.values())
#         save_data(data)

#     return update_data.id

