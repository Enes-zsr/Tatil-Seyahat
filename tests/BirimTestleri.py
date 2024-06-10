from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# ChromeDriver yolunu belirtin
service = webdriver.chrome.service.Service('C:/chromedriver.exe')
service.start()
driver = webdriver.Chrome(service=service)
# Test senaryosu: Ana sayfaya erişim ve bazı temel işlevler
def test_homepage():
    # Ana sayfaya git
    driver.get("https://localhost:44396/")  # Yerel sunucunuzun adresi

    # Ana sayfa başlığını kontrol et
    assert "Tatil & Seyahat" in driver.title
    if(driver.title=="Tatil & Seyahat"):
        print("\n","\nAna sayfaya giriş başarılı\n")

    # Hakkımızda sayfasına git
    hakkimizda_link = driver.find_element(By.LINK_TEXT, "Hakkımızda")
    hakkimizda_link.click()
    assert "Tatil & Seyahat" in driver.title
    print("Hakkımızda sayfasına başarıyla yönlendirildi:", driver.current_url,"\n")

    # Blog sayfasına git
    blog_link = driver.find_element(By.LINK_TEXT, "Bloğum")
    blog_link.click()
    assert "Tatil & Seyahat" in driver.title
    print("Blog sayfasına başarıyla yönlendirildi:", driver.current_url,"\n")


    # İletişim sayfasına git
    iletisim_link = driver.find_element(By.LINK_TEXT, "İletişim")
    iletisim_link.click()
    assert "Tatil & Seyahat" in driver.title
    print("İletişim sayfasına başarıyla yönlendirildi:", driver.current_url, "\n")

    # Admin paneline giriş yap
    driver.get("https://localhost:44396/GirisYap/Login/?ReturnUrl=%2fAdmin")  # Admin panelinin adresi
    driver.find_element(By.ID, "admin").send_keys("Codeus")
    driver.find_element(By.ID, "sifre").send_keys("2003E2007e")

    login_button = driver.find_element(By.TAG_NAME,"input")
    login_button.click()
    assert ("Admin") in driver.title
    print("Admin paneline başarıyla giriş yapıldı.\n")

    driver.get("https://localhost:44396/Default/Index")
    images = driver.find_elements(By.TAG_NAME, "img")

    for img in images:
        if img.get_attribute("src"):
            print("Resim URL'si", img.get_attribute("src"))

        else:
            print("Bu Resim URL'si Yok", img.get_attribute("outerHTML"))

    # Tarayıcıyı kapat
    driver.quit()




