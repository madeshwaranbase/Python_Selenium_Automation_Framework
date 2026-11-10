from pathlib import Path
import pytest
from src.config.settings import settings
from src.core.driver_factory import create_driver
from src.api.rest_client import RestClient

@pytest.fixture
def driver(request):
    browser = create_driver()
    browser.implicitly_wait(0)
    browser.set_window_size(1440, 1000)
    yield browser

    if getattr(request.node, 'rep_call', None) and request.node.rep_call.failed:
        Path("artifacts/screenshots").mkdir(parents=True, exist_ok=True)
        safe_name = request.node.name.replace("/", "_")
        browser.save_screenshot(f"artifacts/screenshots/{safe_name}.png")
    browser.quit()

@pytest.fixture
def api_client():
    return RestClient()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)
