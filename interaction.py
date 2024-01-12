import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# find_element(By.ID, "id")
# find_element(By.NAME, "name")
# find_element(By.XPATH, "xpath")
# find_element(By.LINK_TEXT, "link text")
# find_element(By.PARTIAL_LINK_TEXT, "partial link text")
# find_element(By.TAG_NAME, "tag name")
# find_element(By.CLASS_NAME, "class name")
# find_element(By.CSS_SELECTOR, "css selector")
URL = "https://en.wikipedia.org/wiki/Main_Page"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

chrome_driver_file = "C:\CS_Python100Days\selenium_webdriver\chromedriver.exe"

service = Service(chrome_driver_file)
driver = webdriver.Chrome(options=options, service=service)

driver.get(URL)

articles_count = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")
print(articles_count.text)

# articles_count.click()

# community_portal = driver.find_element(By.LINK_TEXT, "Community portal")
# community_portal.click()
search_icon = driver.find_element(By.CLASS_NAME, "search-toggle")
search_icon.click()
search_bar = driver.find_element(By.NAME, "search")

search_bar.send_keys("bird")
time.sleep(1)
search_button = driver.find_element(By.CLASS_NAME, "cdx-search-input__end-button")
search_button.click()
# the ENTER does not seem works
# search_bar.send_keys(Keys.ENTER)

