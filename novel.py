'''
lab_1 = "/html/body/div[1]/div[6]/div/div[1]/dl/dd[1]"
lab_2 = "/html/body/div[1]/div[6]/div/div[1]/dl/dd[2]"
lab_3 = "/html/body/div[1]/div[6]/div/div[1]/dl/dd[3]/a/cite"
lab_4 = "/html/body/div[1]/div[6]/div/div[1]/dl/dd[4]/a/cite"
lab_5 = "/html/body/div[1]/div[6]/div/div[1]/dl/dd[5]/a/cite"
lab_6 = "/html/body/div[1]/div[6]/div/div[1]/dl/dd[6]/a/cite"
lab_7 = "/html/body/div[1]/div[6]/div/div[1]/dl/dd[7]/a/cite"
lab_8 = "/html/body/div[1]/div[6]/div/div[1]/dl/dd[8]/a/cite"
lab_9 = "/html/body/div[1]/div[6]/div/div[1]/dl/dd[9]/a/cite"
lab_10 = "/html/body/div[1]/div[6]/div/div[1]/dl/dd[10]"
lab_11 = "/html/body/div[1]/div[6]/div/div[1]/dl/dd[11]"
lab_12 = "/html/body/div[1]/div[6]/div/div[1]/dl/dd[12]"
lab_13 = "/html/body/div[1]/div[6]/div/div[1]/dl/dd[13]"
lab_14 = "/html/body/div[1]/div[6]/div/div[1]/dl/dd[14]"

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)
driver.get("https://www.qidian.com/2cy/")
# driver.get("https://www.qidian.com/")

def title():
    driver.find_element(By.XPATH, lab_1).click()
    return(driver.title)

print(title())
driver.quit()
'''