from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("****/selenium/drivers/chromedriver.exe") #ADD HERE TH PATH OF CHROMEDRIVER
driver.set_page_load_timeout(10)
print("abc")
driver.get("https://www.facebook.com/")
driver.find_element_by_id("email").send_keys("WROITE YOU NUMBER OR EMAIML INSIDE THIS DOUBLE QUOTE IN PLACE OF THIS TEXT") 
driver.find_element_by_id("pass").send_keys("WRITE YOUR PASSWORD HERE INSIDE DOUBOE QUOTE IN PLACE OF THIS TEST")
driver.find_element_by_name("login").click()
# driver.find_element_by_id("global_typeahead").send_keys("prasanna anjankar") FOR HPW TO FIND MEON FB BUT TIME  
# KAM HAI TO ITNA HI SUBMIT KAR RA
# driver.find_element_by_id("header-container").click()
time.sleep(4)
driver.quit()
