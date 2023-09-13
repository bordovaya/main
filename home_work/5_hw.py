from selenium import webdriver
from selenium.webdriver.common.by import By # нужен, чтобы искать элементы
from selenium.common.exceptions import NoSuchElementException # поиск ошибок

def test_site_visit():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    try:
        driver.find_element(By.CSS_SELECTOR, '#user-name')
    except NoSuchElementException:
        assert False
    assert True
    try:
        driver.find_element(By.CSS_SELECTOR, '#password')
    except NoSuchElementException:
        assert False
    assert True
    try:
        driver.find_element(By.CSS_SELECTOR, '#login-button')
    except NoSuchElementException:
        assert False
    assert True