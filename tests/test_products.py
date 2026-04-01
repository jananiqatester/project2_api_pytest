"""
This test suite validates product APIs including:
- Retrieval (GET)
- Creation (POST)
- Update (PUT)
- Deletion (DELETE)

Includes both positive and negative scenarios using parametrization.
"""

import pytest
from utils.api_client import get, post
from utils.validators import (
    validate_status_code,
    validate_json_response,
    validate_list_not_empty,
    validate_product_structure
)

# =========================================================
# TC_001 - Verify GET /products returns list of products
# =========================================================
def test_get_products_success():
    response = get("/products")

    if response.status_code == 523:
        pytest.skip("External API unavailable (523)")

    assert response.status_code == 200
    validate_status_code(response, 200)

    data = validate_json_response(response)
    validate_list_not_empty(data)


# =========================================================
# TC_002 - Verify GET /products/{id} with valid ID
# TC_003 - Verify GET /products/{id} with invalid ID
# =========================================================
@pytest.mark.parametrize("product_id", [1, 2, 9999])
def test_get_product_by_id(product_id):

    response = get(f"/products/{product_id}")

    if response.status_code == 523:
        pytest.skip("External API unavailable (523)")

    assert response.status_code in [200, 404]

    data = validate_json_response(response)

    if response.status_code == 200:
        assert data["id"] == product_id
        validate_product_structure(data)

    elif response.status_code == 404:
        assert data == {}


# =========================================================
# TC_004 - Verify POST /products creates a new product
# =========================================================
def test_create_product():
    payload = {
        "title": "Test Product",
        "price": 100,
        "description": "Test description",
        "image": "https://i.pravatar.cc",
        "category": "electronics"
    }

    response = post("/products", payload)

    if response.status_code == 523:
        pytest.skip("External API unavailable (523)")

    assert response.status_code in [200, 201]

    data = validate_json_response(response)

    assert "id" in data
    assert data["title"] == payload["title"]


# =========================================================
# TC_005 - Verify PUT /products/{id} updates product
# =========================================================
def test_update_product():
    from utils.api_client import put

    payload = {
        "title": "Updated Product"
    }

    response = put("/products/1", payload)

    if response.status_code == 523:
        pytest.skip("External API unavailable (523)")

    assert response.status_code == 200


# =========================================================
# TC_006 - Verify DELETE /products/{id} deletes product
# =========================================================
def test_delete_product():
    from utils.api_client import delete

    response = delete("/products/1")

    if response.status_code == 523:
        pytest.skip("External API unavailable (523)")

    assert response.status_code == 200