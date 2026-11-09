from app.schemas import ItemCreate

# 内存存储：id -> item dict
_db: dict[int, dict] = {}
_next_id = 1

def create_item(data: ItemCreate) -> dict:
    global _next_id
    item = {"id": _next_id, **data.model_dump()}
    _db[_next_id] = item
    _next_id += 1
    return item

def get_item(item_id: int) -> dict | None:
    return _db.get(item_id)

def list_items(skip: int = 0, limit: int = 100) -> list[dict]:
    return list(_db.values())[skip : skip + limit]

def update_item(item_id: int, data: dict) -> dict | None:
    if item_id not in _db:
        return None
    _db[item_id].update(data)
    return _db[item_id]

def delete_item(item_id: int) -> bool:
    return _db.pop(item_id, None) is not None
