import chromedriver_binary
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


search_command = input()
search_command = str(search_command)


browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://www.104.com.tw/jobs/main/")

searcher = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, "ikeyword")))

searcher.send_keys(search_command)

searcher_button = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button.btn.btn-primary.js-formCheck')))




searcher_button.click()

sleep(60)
browser.close()
