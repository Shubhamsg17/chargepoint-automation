from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os, time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

EMAIL = os.getenv("CHARGEPOINT_EMAIL")
PASSWORD = os.getenv("CHARGEPOINT_PASSWORD")

chrome_options = Options()
# Comment headless to see it working visually
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=chrome_options)

try:
    print("Logging into ChargePoint...")
    driver.get("https://na.chargepoint.com/login")
    driver.save_screenshot("1_initial_page.png")

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username")))
    driver.find_element(By.ID, "username").send_keys(EMAIL)

    driver.save_screenshot("2_initial_page.png")
    element = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '[data-qa-id="form_submit_button"]')))
    element.click()


    driver.save_screenshot("3_initial_page.png")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    element = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '[data-qa-id="form_submit_button"]')))
    element.click()
    driver.save_screenshot("2_after_submit.png")

    WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".sc-dlWCHZ.cBOeKh")))
    print("Login successful")

    driver.get("https://driver.chargepoint.com/waitlist")
    element = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '[data-qa-id="join_waitlist_button"]')))
    element.click()

    element = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.sc-kdBSHD gzvvUJ')))
    element.click()
    

    print("Join Waitlist successful")

    element = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.sc-ixPHmS gBLpfA')))
    element.click()

    element = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.sc-dlWCHZ cBOeKh')))
    element.click()


except Exception as e:
    print(f"Script failed: {e}")
    driver.save_screenshot("error.png")

finally:
    driver.quit()


