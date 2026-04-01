# \# API Testing Project (Pytest)



### \## Overview



This project demonstrates API testing using Python, Pytest, and Requests library.



It covers:



\* CRUD operations testing (GET, POST)

\* Positive and negative test scenarios

\* Parameterized testing

\* Reusable API client and validators



\---

### 

### \## Tech Stack



\* Python

\* Pytest

\* Requests



\---



### \## Project Structure



```

project2\_api\_pytest/

│

├── tests/

│   ├── test\_products.py

│   └── test\_auth.py

│

├── utils/

│   ├── api\_client.py

│   └── validators.py

│

├── config/

│   └── config.py

│

├── requirements.txt

└── README.md

```



\---



### \## Test Coverage



\* GET all products

\* GET product by ID (valid \& invalid)

\* POST create product

\* Authentication (login API)



\---



### \## Note



Tests may fail with status code \*\*523\*\* due to FakeStore API downtime.

This is an external service issue, not a defect in the test implementation.



\---



### \## How to Run



```

pip install -r requirements.txt

pytest -v

```



