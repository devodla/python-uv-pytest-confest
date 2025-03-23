from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_main():
    response = client.get("/")
    assert response.status_code == 200, "The response status code should be 200."
    assert response.text == "Hello from FastAPI", (
        """The response text should be "Hello from FastAPI"."""
    )
