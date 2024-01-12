from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service = Service("C:\CS_Python100Days\selenium_webdriver\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=service)

# driver.get("https://www.amazon.com/gp/product/B07XXNY4GG/ref=ox_sc_saved_image_2?smid=AMY4I718ZUBOU&psc=1")
# price = driver.find_element(by=By.CLASS_NAME, value="a-offscreen")
# print(price.get_attribute("textContent"))

driver.get("https://www.python.org/")
search_bar = driver.find_element(by=By.NAME, value="q")
print(search_bar.get_attribute("placeholder"))
print(search_bar.tag_name)

logo = driver.find_element(by=By.CLASS_NAME, value="python-logo")
print(logo.size)

documentation_link = driver.find_element(by=By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)

website_bug = driver.find_element(by=By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(website_bug.text)

events_times = driver.find_elements(by=By.CSS_SELECTOR, value='.event-widget time')
events_names = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget li a")
events = {}
for n in range(len(events_names)):
    events[n] = {
        "time": events_times[n].text,
        "name": events_names[n].text
    }

print(events)


driver.close()