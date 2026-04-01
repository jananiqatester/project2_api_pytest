def validate_status_code(response, expected_code):
    assert response.status_code == expected_code

def validate_json_response(response):
    try:
        return response.json()
    except Exception:
        assert False, "Response is not valid JSON"

def validate_list_not_empty(data):
    assert isinstance(data, list)
    assert len(data) > 0

def validate_product_structure(product):
    assert "id" in product
    assert "title" in product
    assert "price" in product
    assert "category" in product