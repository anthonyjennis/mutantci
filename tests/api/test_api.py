from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_quote_endpoint():
    response = client.post("/quote", json={"total": 2500})

    assert response.status_code == 200
    assert response.json() == {
        "total": 2500,
        "shipping_fee": 0,
        "gst_percent": 12,
        "discount_percent": 10,
    }


def test_quote_rejects_negative_total():
    response = client.post("/quote", json={"total": -100})

    assert response.status_code == 422
