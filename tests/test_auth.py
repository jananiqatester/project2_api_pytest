from utils.api_client import login
import pytest

# =========================================================
# TC_001 - Verify login returns token for valid credentials
# =========================================================
def test_login_success():
    response = login(TEST_USERNAME, TEST_PASSWORD)

    # Handle external API downtime
    if response.status_code == 523:
        pytest.skip("External API unavailable (523)")

    assert response.status_code == 200

    data = response.json()

    assert "token" in data
    assert isinstance(data["token"], str)