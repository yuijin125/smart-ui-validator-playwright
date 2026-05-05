# Smart UI Validation Framework

A Playwright + PyTest based UI automation framework using Page Object Model (POM), data-driven testing, and dynamic test execution.

---

## 🚀 Overview

This project is a scalable UI automation framework built using Python, Playwright, and PyTest.  
It automates end-to-end workflows such as login, product handling, and cart validation.

The framework follows the Page Object Model (POM) and supports data-driven testing using JSON, making it maintainable and extensible.

---

## 🛠️ Tech Stack

- Python  
- Playwright  
- PyTest  
- JSON  
- pytest-html  
- requests (API testing)  

---

## ✅ Features

- Login automation (valid & invalid scenarios)  
- Add and remove products from cart  
- Multiple product validation  
- Data-driven testing using JSON  
- Dynamic test execution using PyTest parametrization  
- Product extraction (UI → JSON)  
- Basic API validation  
- HTML reporting  

---

## 📁 Project Structure
smart-ui-validator/
├── pages/        # Page Object Model (UI actions)
├── tests/        # Test cases
├── core/         # Utilities (loader, validator, api)
├── data/         # JSON test data
├── conftest.py   # Fixtures
├── pytest.ini
├── requirements.txt
└── README.md


---

## ▶️ How to Run

### Install dependencies

pip install -r requirements.txt  
playwright install  

---

### Run tests

pytest -v  

---

### Debug mode

pytest -v --headed --slowmo=1000  

---

### Parallel execution

pytest -n 2 -v  

---

## 🧠 Key Concepts

- Page Object Model (POM)  
- Data-driven testing  
- PyTest fixtures and parametrization  
- Dynamic locators in Playwright  
- UI + API validation approach  

---

## 👨‍💻 Author

Pavan Prasad K S
