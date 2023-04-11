from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# options = Options()
# options.add_argument('headless')
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()

driver.get("https://www.bing.com")
print(driver.title)

driver.quit()