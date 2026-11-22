from fastapi import FastAPI

app = FastAPI()

# A fake database: a list of dictionaries
items_db = [
    {"id": 1, "name": "Laptop", "price": 55000, "category": "electronics"},
    {"id": 2, "name": "Phone", "price": 20000, "category": "electronics"},
    {"id": 3, "name": "Notebook", "price": 50, "category": "stationery"},
    {"id": 4, "name": "Pen", "price": 10, "category": "stationery"},
    {"id": 5, "name": "Headphones", "price": 3000, "category": "electronics"},
]


# 1. Path parameter
@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items_db:
        if item["id"] == item_id:
            return item
    return {"error": "Item not found"}


# 2. Query parameters with defaults (pagination)
@app.get("/items")
def list_items(skip: int = 0, limit: int = 10):
    return items_db[skip : skip + limit]


# 3. Optional query parameter (filtering)
@app.get("/search")
def search_items(category: str | None = None, max_price: int | None = None):
    results = items_db
    if category:
        results = [i for i in results if i["category"] == category]
    if max_price:
        results = [i for i in results if i["price"] <= max_price]
    return results


# 4. Path + query parameter together
@app.get("/users/{user_id}/items")
def user_items(user_id: int, limit: int = 2):
    return {"user_id": user_id, "items": items_db[:limit]}