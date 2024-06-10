from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ChromeDriver yolunu belirtin
service = webdriver.chrome.service.Service('C:/chromedriver.exe')
service.start()
driver = webdriver.Chrome(service=service)


def test_successful_login():
    # Doğru kullanıcı adı ve şifre ile giriş yapma senaryosu
    driver.get("https://localhost:44396/Admin")

    # Kullanıcı adı ve şifreyi gir
    username_input = driver.find_element(By.ID, "admin")
    username_input.send_keys("Codeus")

    password_input = driver.find_element(By.ID, "sifre")
    password_input.send_keys("2003E2007e")

    # Giriş yap butonuna tıkla
    login_button = driver.find_element(By.TAG_NAME, "input")
    login_button.click()

    # Başlığı kontrol et
    assert "Admin" in driver.title
    print("Doğru kullanıcı adı ve şifre ile giriş yapıldı.\n")


def test_successful_Index():
    # Doğru kullanıcı adı ve şifre ile giriş yapma senaryosu
    driver.get("https://localhost:44396/Admin")

    # Kullanıcı adı ve şifreyi gir
    username_input = driver.find_element(By.ID, "admin")
    username_input.send_keys("Codeus")

    password_input = driver.find_element(By.ID, "sifre")
    password_input.send_keys("2003E2007e")

    # Giriş yap butonuna tıkla
    login_button = driver.find_element(By.TAG_NAME, "input")
    login_button.click()

    # Hakkımızda linkini bulmak için bekleme süresi ekleyerek tekrar dene
    try:
        hakkimizda_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Hakkımızda')]")))
        hakkimizda_link.click()

        # Başlığı kontrol et
        assert "Tatil & Seyahat" in driver.title
        print("Hakkımızda sayfasına başarıyla yönlendirildi:", driver.current_url, "\n")

    except Exception as e:
        print("Hakkımızda linki bulunamadı veya tıklanamadı.")
        print(e)


# Test senaryolarını çalıştır
test_successful_login()
test_successful_Index()

# WebDriver'ı kapat
driver.quit()