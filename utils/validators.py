def validate_status_code(response, expected_code):
    assert response.status_code == expected_code, \
        f"Expected {expected_code}, got {response.status_code}"

def validate_json_response(response):
    try:
        return response.json()
    except Exception:
        assert False, "Response is not valid JSON"

def validate_list_not_empty(data):
    assert isinstance(data, list), "Response is not a list"
    assert len(data) > 0, "Response list is empty"

def validate_product_structure(product):
    assert "id" in product, "Missing 'id'"
    assert "title" in product, "Missing 'title'"
    assert "price" in product, "Missing 'price'"
    assert "category" in product, "Missing 'category'"