from pydantic import BaseModel, Field

class ItemBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=50, description="物品名称")
    price: float = Field(..., gt=0, description="价格，必须大于 0")
    description: str | None = Field(None, max_length=200)

class ItemCreate(ItemBase):
    """创建时的请求体"""

class ItemUpdate(BaseModel):
    """更新时的请求体（所有字段可选）"""
    name: str | None = Field(None, min_length=1, max_length=50)
    price: float | None = Field(None, gt=0)
    description: str | None = None

class Item(ItemBase):
    """返回给客户端的完整对象"""
    id: int
