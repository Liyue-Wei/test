from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import time

os.popen('start chrome --remote-debugging-port=9527 --user-data-dir="C:\chromedriver_win32"')
opt = Options()
# opt.add_argument('--headless')
opt.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
driver = webdriver.Chrome(options=opt)

driver.get("https://zh.wikipedia.org/zh-tw/%E4%B8%AD%E6%96%87%E7%B7%A8%E7%A8%8B%E8%AA%9E%E8%A8%80")
test = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[5]/div[1]/p[2]/mark/a[1]").click()

# driver.get("https://act.hoyolab.com/bbs/event/signin/hkrpg/index.html?act_id=e202303301540311&hyl_auth_required=true&hyl_presentation_style=fullscreen&utm_source=hoyolab&utm_medium=tools&utm_campaign=checkin&utm_id=6&lang=zh-tw&bbs_theme=light&bbs_theme_device=1")
# day = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[3]/div/div[1]/div[2]/button")   
# print(day)

'''
time.sleep(0.5)
driver.quit()
# driver.close()
'''