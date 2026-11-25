from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

items_db = []


# 1. Basic model
class Item(BaseModel):
    name: str
    price: float
    category: str = "general"          # optional, has a default
    description: str | None = None     # optional, can be missing


# 2. Model with validation rules
class User(BaseModel):
    username: str = Field(min_length=3, max_length=20)
    email: str
    age: int = Field(ge=13, le=100)    # ge = greater or equal, le = less or equal


# POST with a request body
@app.post("/items")
def create_item(item: Item):
    items_db.append(item)
    return {"message": "Item created", "item": item}


# GET to see what was saved
@app.get("/items")
def list_items():
    return items_db


# Body + path parameter together
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "updated_item": item}


# Body + path + query together
@app.post("/users/{team_id}")
def create_user(team_id: int, user: User, notify: bool = False):
    return {"team_id": team_id, "notify": notify, "user": user}
  
