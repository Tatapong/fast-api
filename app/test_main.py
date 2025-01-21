from fastapi.testclient import TestClient
from main import app  # Ensure this is correct if the app is in the same directory

client = TestClient(app)

def test_read_main():
    response = client.get("/")  # Ensure this is the correct endpoint
    assert response.status_code == 200
    assert response.json() == {"msg": "FIN DE LA DEMO DEVOPS"}
