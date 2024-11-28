import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


i = 1
print("Kører loop nummer " + str(i))
    
nummer = 1  # Initialize the variable 'nummer'
nummer = nummer + 1

email = "JakobKvejborglol+" + str(nummer) + "@gmail.com"
url = "https://www.arla.dk/produkter/arlaoko/pakkeleg/"

service = Service("C:\\Program Files\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get(url)

# Increase wait time to make sure everything is loaded
driver.implicitly_wait(20)

# Wait for the cookie button to be clickable and click it
cookie_button = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.ID, "accept-recommended-btn-handler"))
)
cookie_button.click()
print("Cookie button clicked")


# Wait for the SPIL HER button to appear then click it
SPILHER_button = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, "button.lf-button__element"))
)
SPILHER_button.click()
print("Next button clicked")

  

    # Keep the browser open
input("Press Enter to close the browser...")
 
