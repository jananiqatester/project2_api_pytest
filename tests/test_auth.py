import pytest

from utils.api_client import login
from config.config import TEST_USERNAME, TEST_PASSWORD


# =========================================================
# TC_001 - Verify login returns token for valid credentials
# =========================================================
def test_login_success():
    response = login(TEST_USERNAME, TEST_PASSWORD)

    # Handle external API downtime
    if response.status_code == 523:
        pytest.skip("External API unavailable (523)")

    assert response.status_code in [200, 201]

    data = response.json()

    assert "token" in data
    assert isinstance(data["token"], str)