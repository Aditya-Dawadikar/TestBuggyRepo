from fastapi import FastAPI, HTTPException
import random
import time
from typing import Dict, List

app = FastAPI()

class CustomServerError(Exception):
    pass

def random_failure(failure_rate: float = 0.3) -> bool:
    return random.random() < failure_rate

@app.get("/")
async def root():
    return {"message": "Welcome to the Buggy Server!"}

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    if random_failure():
        errors = [
            HTTPException(status_code=404, detail="User not found"),
            HTTPException(status_code=500, detail="Internal server error"),
            CustomServerError("Unexpected server malfunction"),
            ValueError("Invalid user ID format"),
            TimeoutError("Database connection timeout")
        ]
        raise random.choice(errors)
    
    return {"user_id": user_id, "name": f"User {user_id}", "status": "active"}

@app.post("/items/")
async def create_item(item: Dict[str, str]):
    if random_failure(0.4):
        # Simulate various server-side issues
        if random.random() < 0.5:
            time.sleep(10)  # Random delay
            raise HTTPException(status_code=504, detail="Gateway Timeout")
        else:
            raise HTTPException(status_code=400, detail="Invalid item format")
    
    return {"item_id": random.randint(1, 1000), **item}

@app.get("/products")
async def list_products():
    if random_failure(0.35):
        errors = [
            KeyError("Product cache not initialized"),
            MemoryError("Out of memory while processing request"),
            HTTPException(status_code=503, detail="Service temporarily unavailable")
        ]
        raise random.choice(errors)
    
    products = [
        {"id": i, "name": f"Product {i}", "price": random.randint(10, 100)}
        for i in range(1, 6)
    ]
    return products

@app.put("/update/{item_id}")
async def update_item(item_id: int, data: Dict[str, str]):
    if random_failure(0.45):
        if random.random() < 0.3:
            # Simulate database connection issues
            raise ConnectionError("Database connection lost")
        elif random.random() < 0.6:
            raise HTTPException(status_code=409, detail="Conflict in update operation")
        else:
            raise HTTPException(status_code=422, detail="Unprocessable Entity")
    
    return {"item_id": item_id, "status": "updated", **data}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)