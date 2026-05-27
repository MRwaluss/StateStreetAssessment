from pathlib import Path
import platform
from typing import Generator, List

import allure
from pytest import fixture

from Tests.pages.app_page import AppPage
from playwright.sync_api import sync_playwright, Browser, Page, Playwright

@fixture(scope="session")
def python_executable() -> Generator[str, None, None]:
    with allure.step("Checking system type"):
        os_type = platform.system()
        python = "python3"
        if os_type == "Windows":
            python = "python"
        yield python

@fixture(scope="session")
def main_cli_app_filepath() -> Generator[Path, None, None]:
    with allure.step("Retreive application executive file"):
        yield Path.cwd().parent / "App/assessment_cli.py"

@fixture(scope="function")
def run_command(main_cli_app_filepath: Path, 
                python_executable: str,
                total_asset: str,
                security: str,
                target: str,
                current: str,
                unit_price: str) -> Generator[List[str], None, None]:
    with allure.step("Build application run command"):
        cmd = [python_executable, main_cli_app_filepath]
        cmd += [
                "--total_asset", total_asset,
                "--security", security,
                "--target", target,
                "--current", current,
                "--unit_price", unit_price,
            ]  
        yield cmd

@fixture(scope="function")
def total_asset(request) -> Generator[str, None, None]:
    yield request.param
    
@fixture(scope="function")
def security(request) -> Generator[str, None, None]:
    yield request.param
    
@fixture(scope="function")
def target(request) -> Generator[str, None, None]:
    yield request.param
    
@fixture(scope="function")
def current(request) -> Generator[str, None, None]:
    yield request.param
    
@fixture(scope="function")
def unit_price(request) -> Generator[str, None, None]:
    yield request.param

@fixture(scope="session")
def playwright_instance() -> Generator[Playwright, None, None]:
    with sync_playwright() as playwright:
        yield playwright

@fixture(scope="session")
def browser(playwright_instance) -> Generator[Browser, None, None]:
    browser = playwright_instance.chromium.launch(
        headless=False
    )
    yield browser
    browser.close()

@fixture(scope="function")
def page(browser: Browser) -> Generator[Page, None, None]:
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@fixture(scope="function")
def login_page(page: Page)-> Generator[AppPage, None, None]:
    app_page = AppPage(page)
    app_page.open()
    yield app_page