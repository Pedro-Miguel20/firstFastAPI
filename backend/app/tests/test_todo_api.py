from app.main import app
from starlette.testclient import TestClient

client = TestClient(app)


def test_call_endpoint():
    response = client.get("/todos")
    assert response.status_code == 200