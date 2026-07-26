from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class RequestData(BaseModel):
    old_price: float
    new_price: float
    days_remaining: int
    days_in_actual_month: int
    spec: str

@app.post("/prorate")
def prorate(data: RequestData):
    delta = data.new_price - data.old_price

    if data.spec == "v1":
        charge = delta * (data.days_remaining / 30)
    else:
        charge = delta * (data.days_remaining / data.days_in_actual_month)

    return {"charge": round(charge, 2)}
