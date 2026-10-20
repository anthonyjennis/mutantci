"""FastAPI application for the MutantCI pricing demo."""

from fastapi import FastAPI
from pydantic import BaseModel, Field

from core.rules import discount_percent, gst_percent, shipping_fee

app = FastAPI(title="MutantCI Pricing API")


class QuoteRequest(BaseModel):
    total: int = Field(ge=0, description="Order total in whole rupees")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/quote")
def create_quote(request: QuoteRequest):
    total = request.total
    return {
        "total": total,
        "shipping_fee": shipping_fee(total),
        "gst_percent": gst_percent(total),
        "discount_percent": discount_percent(total),
    }
