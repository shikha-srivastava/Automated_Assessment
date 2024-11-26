import os
import os.path
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_binary = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"


# setup and tear down
@pytest.fixture(scope="function")
def driver(request):
    options = webdriver.ChromeOptions()
    options.binary_location = chrome_binary
    options.add_argument("start-maximized")

    driver = webdriver.Chrome(
        service=Service("C:/Users/Kushagra/PycharmProjects/chromedriver-win64/chromedriver.exe"),
        options=options
    )
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
