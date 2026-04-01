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

    # Validate status code
    assert response.status_code == 200
    validate_status_code(response, 200)

    # Validate response is JSON and not empty
    data = validate_json_response(response)
    validate_list_not_empty(data)


# =========================================================
# TC_002 - Verify GET /products/{id} with valid ID
# TC_003 - Verify GET /products/{id} with invalid ID
# =========================================================
@pytest.mark.parametrize("product_id", [1, 2, 9999])
def test_get_product_by_id(product_id):

    response = get(f"/products/{product_id}")

    # Validate status code (200 for valid, 404 for invalid)
    assert response.status_code in [200, 404]

    data = validate_json_response(response)

    # Positive case: valid product
    if response.status_code == 200:
        assert data["id"] == product_id
        validate_product_structure(data)

    # Negative case: invalid product
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

    # Validate creation status
    assert response.status_code in [200, 201]

    data = validate_json_response(response)

    # Validate response contains expected fields
    assert "id" in data
    assert data["title"] == payload["title"]