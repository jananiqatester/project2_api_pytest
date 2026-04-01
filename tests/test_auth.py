from utils.api_client import login

def test_login_success():
    response = login("mor_2314", "83r5^_")

    assert response.status_code == 200

    data = response.json()

    assert "token" in data
    assert isinstance(data["token"], str)