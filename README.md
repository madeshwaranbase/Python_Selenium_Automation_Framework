# GreenKart UI & API Automation Framework

A maintainable Python test automation framework for the [GreenKart practice application](https://rahulshettyacademy.com/seleniumPractise/#/).

## Scope
- UI automation: product search, adding products to cart, cart validation and checkout.
- REST API automation: configurable Requests-based API checks.
- PyTest fixtures, parametrization, Page Object Model and pytest-bdd.
- Failure screenshots, structured logging and HTML reports.
- GitHub Actions CI workflow.

> **API note:** GreenKart is used for the browser workflows. It does not publish a stable public API contract alongside this practice URL. The API suite therefore targets JSONPlaceholder by default as a separately configurable REST test target. Replace `API_BASE_URL` and endpoint/test data when integrating a documented application API. Do not represent these API checks as GreenKart backend coverage.

## Requirements
- Python 3.10+
- Google Chrome
- Git

## Quick start
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Selenium Manager resolves the browser driver automatically in supported Selenium versions.

## Run tests
```bash
# All tests
pytest

# UI only
pytest -m ui

# API only
pytest -m api

# BDD scenarios
pytest -m bdd

# Browser UI with visible browser
HEADLESS=false pytest -m ui

# HTML report
pytest --html=artifacts/report.html --self-contained-html
```

## Configuration
Configuration is loaded from environment variables (or `.env` locally).

| Variable | Default | Purpose |
|---|---|---|
| `BASE_URL` | GreenKart URL | Browser application |
| `BROWSER` | `chrome` | Browser selection |
| `HEADLESS` | `true` | Headless execution |
| `WAIT_TIMEOUT` | `10` | Explicit wait timeout |
| `API_BASE_URL` | JSONPlaceholder | REST API target |
| `API_TIMEOUT` | `15` | API request timeout |

Never commit credentials or environment-specific secrets.

## Repository structure
```text
src/
  config/       Environment-backed settings
  core/         Driver lifecycle, waits, logging
  pages/        Page objects and page components
  api/          Requests client
tests/
  ui/           Browser tests
  api/          REST API tests
  bdd/           Gherkin feature and step definitions
```

## Engineering conventions
- Tests assert user-visible outcomes, not implementation details.
- Locators are centralized in page objects.
- Explicit waits are preferred over sleeps.
- Test data is isolated and generated per test where possible.
- API assertions validate status, schema shape and business-relevant fields.
- CI publishes the HTML report even when a test fails.

## Known limitations
The practice application can change its markup without notice. If a locator changes, update the relevant page object rather than the test. The sample API checks use JSONPlaceholder and are intentionally independent from GreenKart UI tests.

## Suggested extensions
- Add Allure reporting and test history.
- Add Dockerized browser execution.
- Add contract/schema validation for a documented API.
- Add parallel execution after confirming test-data isolation.


## CI and repository governance
The included GitHub Actions workflow runs the test suite on pushes and pull requests and uploads reports as workflow artifacts. Protect the default branch with required pull-request review and passing checks after publishing this repository.

## Test evidence
The framework source is provided as a portfolio starter. Execute it against the live practice application before publishing any pass-rate, test-count or execution-time claims. Practice-site markup and availability are outside this repository's control.
