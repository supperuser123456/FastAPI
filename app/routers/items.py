from fastapi import APIRouter, HTTPException, Query, status

from app import models
from app.schemas import Item, ItemCreate, ItemUpdate

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/", response_model=list[Item])
def list_items(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
):
    return models.list_items(skip=skip, limit=limit)

@router.get("/{item_id}", response_model=Item)
def get_item(item_id: int):
    item = models.get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.post("/", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(payload: ItemCreate):
    return models.create_item(payload)

@router.patch("/{item_id}", response_model=Item)
def update_item(item_id: int, payload: ItemUpdate):
    # exclude_unset：只传要改的字段
    data = payload.model_dump(exclude_unset=True)
    item = models.update_item(item_id, data)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    if not models.delete_item(item_id):
        raise HTTPException(status_code=404, detail="Item not found")
