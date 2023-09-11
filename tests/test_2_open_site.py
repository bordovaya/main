from selenium import webdriver
from selenium.webdriver.common.by import By # нужен, чтобы искать элементы
from selenium.common.exceptions import NoSuchElementException # поиск ошибок

def test_site_visit():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/")

    try:
        driver.find_element(By.CSS_SELECTOR, 'header > a > img')
    except NoSuchElementException:
        assert False
    assert True