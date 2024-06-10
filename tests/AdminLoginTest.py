from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# ChromeDriver yolunu belirtin
service = webdriver.chrome.service.Service('C:/chromedriver.exe')
service.start()
driver = webdriver.Chrome(service=service)


def test_successful_login():
    driver.get("https://localhost:44396/GirisYap/Login/?ReturnUrl=%2fAdmin")  # Admin panelinin adresi
    driver.find_element(By.ID, "admin").send_keys("Codeus")
    driver.find_element(By.ID, "sifre").send_keys("2003E2007e")

    login_button = driver.find_element(By.TAG_NAME, "input")
    login_button.click()
    assert ("Admin") in driver.title
    print("Admin paneline başarıyla giriş yapıldı.\n")

# Test senaryolarını çalıştır
test_successful_login()

# WebDriver'ı kapat
driver.quit()