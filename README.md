# FakeStore API Test Framework — Python + Pytest

## Project Overview
A modular API test automation framework built using Python and Pytest, 
targeting the FakeStore public API. Designed to demonstrate real-world 
QA engineering practices including reusable utilities, config-driven 
credentials, and graceful handling of external API inconsistencies.

---

## Tech Stack
- Python
- Pytest
- Requests Library
- Git / GitHub

---

## Project Structure
FakeStore-API-Pytest-Framework/
│
├── tests/
│   ├── test_products.py      # Product API tests (GET, POST, PUT, DELETE)
│   └── test_auth.py          # Authentication tests (login success/failure)
│
├── utils/
│   ├── api_client.py         # Reusable HTTP request functions
│   └── validators.py         # Reusable assertion/validation functions
│
├── config/
│   └── config.py             # Base URL and test credentials
│
├── conftest.py               # Path configuration for Pytest
├── requirements.txt          # Project dependencies
└── README.md
---

## Test Coverage

### Product Tests
- GET all products — validates status 200 and non-empty list
- GET product by valid ID (1, 2) — validates structure and data
- GET product by invalid ID (9999) — handles empty response gracefully
- POST create product — validates 201/200 and response body
- PUT update product — validates status and updated title
- DELETE product — validates status and response confirmation

### Authentication Tests
- Login with valid credentials — validates token returned
- Login with invalid credentials — validates 400/401 response

---

## Key Engineering Decisions

**Reusable API Client** — All HTTP methods centralised in api_client.py. 
Single place to change base URL or headers.

**Validator Utilities** — Assertion logic separated from test logic. 
Cleaner, maintainable, reusable across test files.

**Config-driven Credentials** — Test username and password stored in 
config.py, not hardcoded in test files.

**Graceful API Inconsistency Handling** — FakeStore API returns HTTP 200 
with empty body for non-existent product ID 9999 instead of expected 404. 
Framework detects and skips this with a clear message rather than 
crashing.

**External Downtime Handling** — All tests handle 523 status gracefully 
using pytest.skip() to distinguish infrastructure issues from test 
failures.

---

## How to Run

```bash
pip install -r requirements.txt
pytest -v
```

## Expected Output
- 7 tests PASSED
- 1 test SKIPPED (API inconsistency on ID 9999 — documented behaviour)

---

## Author
Janani Jayarajan
QA Engineer | ISTQB CTFL | AT*SQA API Testing Certified
GitHub: https://github.com/jananiqatester
