from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import BaseModel

app = FastAPI()

class Order(BaseModel):
    book_title: str
    customer_address: str

orders = {}

@app.post("/orders/")
async def create_order(order: Order):
    order_id = len(orders) + 1
    orders[order_id] = {"status": "pending"}
    return {"order_id": order_id}

@app.get("/orders/{order_id}")
async def get_order_status(order_id: int):
    if order_id not in orders:
        raise HTTPException(status_code=404, detail="Order not found")
    return orders[order_id]

def get_current_user(token: str = Depends(oauth2_scheme)):
    # Decode the JWT token to get the user information
    # ... (token decoding logic)
    return user_data

@app.post("/orders/", dependencies=[Depends(get_current_user)])
async def create_order(order: Order, user_data: User = Depends(get_current_user)):
    # Check user permissions here, e.g., if user_data.role == "customer":
    # ... (create order logic)