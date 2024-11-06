import os
import os.path
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_binary = "C:/Program Files/Google/Chrome/Application/chrome.exe"


@pytest.fixture(scope="function")
def driver(request):
    options = Options()
    options.add_argument("--autoplay-policy=no-user-gesture-required")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://indeedemo-fyc.watch.indee.tv/")
    request.cls.driver = driver
    try:
        yield driver
    finally:
        driver.quit()


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    report_dir = os.path.join(os.getcwd(), "Html_Report")
    os.makedirs(report_dir, exist_ok=True)
    config.option.htmlpath = os.path.join(report_dir, datetime.now().strftime("%d-%m-%Y_%H-%M-%S") + ".html")
