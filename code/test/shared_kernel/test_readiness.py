import pytest


@pytest.mark.integration
def test_readiness(client):
    response = client.get("/readiness")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}
