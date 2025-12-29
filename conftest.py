import sys
import os
# הוספת תיקיית השורש של הפרויקט ל-Path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def inventory_page(page):
    return InventoryPage(page)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot_path = f"reports/screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path)
            # הוספת התמונה לדיווח ה-HTML
            import pytest_html
            extra.append(pytest_html.extras.image(screenshot_path))
    report.extra = extra