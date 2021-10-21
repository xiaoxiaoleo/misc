from selenium import webdriver

import time
from HDwallet import HDWallet_01
from selenium.webdriver.chrome.options import Options 

receive_lst = HDWallet_01.print_addr_lst(1000, 1060)

for i in receive_lst:
    chrome_options = Options() 
    chrome_options.add_argument("--headless") 
    driver = webdriver.Chrome(executable_path= '/Users/mac/Downloads/chromedriver', options=chrome_options)
    
 
    driver.get("your refer link ") 
    time.sleep(6) 
 
    driver.find_element_by_css_selector("#airdrop-form > div > input").send_keys(f"{i}")
    # 点击搜索按钮
    elem = driver.find_element_by_css_selector("#airdrop-form > div > button")
    elem.send_keys("\n")
 
    driver.quit()
