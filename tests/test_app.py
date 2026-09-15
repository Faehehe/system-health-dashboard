import os

os.environ["APP_ENVIRONMENT"] = "test"

from app import app


def test_health():
    client = app.test_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "UP"}


def test_version():
    client = app.test_client()
    resp = client.get("/version")
    assert resp.status_code == 200
    assert resp.get_json()["version"] == "1.0.0"


def test_environment():
    client = app.test_client()
    resp = client.get("/environment")
    assert resp.status_code == 200
    assert resp.get_json()["environment"] == "test"