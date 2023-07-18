from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

os.popen('start chrome --remote-debugging-port=9527 --user-data-dir="C:\chromedriver_win32"')
opt = Options()
opt.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
driver = webdriver.Chrome(options=opt)

driver.get("https://chromedriver.chromium.org/downloads")