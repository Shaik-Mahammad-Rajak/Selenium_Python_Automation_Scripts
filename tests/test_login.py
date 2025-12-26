import time

from conftest import base_url
from pages.login_page import LoginPage

def test_login(driver, base_url, credentials):
    login = LoginPage(driver)
    login.load(base_url)
    login.login(credentials["username"], credentials["password"])
    time.sleep(5)
    assert "wrong_url" in driver.current_url, "login Failed - URL Does not match"
