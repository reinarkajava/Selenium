from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  # Importige Chrome valikud
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Paneme testikoodi try bloki sisse, et saada tagasisidet, kui midagi läheb nihu
try:
    # Määrame unikaalse andmekausta tee
    user_data_dir = os.path.join(os.getcwd(), "chrome_data")  # Loome kausta töökaustas

    # Loome Chrome'i valikud ja määrame andmekausta
    chrome_options = Options()

    # Programm peab kasutama chrome'i veebidraiverit
    driver = webdriver.Chrome(options=chrome_options)

    # Driver avab google.com lehe
    driver.get("https://www.google.com")

    # Draiver ootab 10 sekundit kuni tekib kypsiste sulgemiseks vajalik nupp.
    try:
        accept_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button//div[contains(text(), 'Keeldu kõigist')]"))
        )
        accept_button.click()
    except Exception as e:
        print(f"Cookie modal not found: {e}")

    # Programm leiab otsinguriba, sisestab teksti ning k2ivitab otsingu
    search_bar = driver.find_element(By.NAME, "q")
    search_bar.send_keys("Seleniumiga otsingu automatiseerimine")
    search_bar.submit()

    # Oota 5 sekundit
    time.sleep(5)

    # Prindi lehe title
    print("Page Title:", driver.title)

    # Sulgege driveri brauser
    driver.quit()

# Kui midagi läheb nihu, siis prindi veateade
except Exception as e:
    print(f"Error: {e}")
