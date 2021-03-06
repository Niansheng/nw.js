import time
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("nwapp=" + os.path.dirname(os.path.abspath(__file__)))

driver = webdriver.Chrome(executable_path=os.environ['CHROMEDRIVER'], chrome_options=chrome_options)
time.sleep(1)
try:
    print driver.current_url
    result = driver.find_element_by_id('result').get_attribute('innerHTML')
    result2 = driver.find_element_by_id('result2').get_attribute('innerHTML')
    print result
    print result2
    assert(result == 'success from popup' and result2 == 'startiframe')
finally:
    #time.sleep(50)
    driver.quit()
