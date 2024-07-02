from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# driver = webdriver.Chrome()
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("https://demo.nopcommerce.com")
driver.maximize_window()
print(driver.title)

driver.find_element(By.ID, "small-searchterms").send_keys("Lenovo")

time.sleep(3)

driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(5)

driver.find_element(By.LINK_TEXT, "Electronics").click()
driver.find_element(By.LINK_TEXT, "Cell phones").click()


driver.close()

