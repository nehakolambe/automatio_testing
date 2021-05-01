from selenium import webdriver
import time

driver = webdriver.Chrome("D:/Labs/ITL/Testing/chromedriver.exe")
driver.get("https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp")

#Locating By ID
driver.find_element_by_id("firstName").send_keys("john")
#Locating By Name
driver.find_element_by_name("lastName").send_keys("watson")
#Locating By XPath
driver.find_element_by_xpath('//*[@id="username"]').send_keys("john.watson982548")
#Locating By Full XPath
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[1]/div/div/div[1]/div/div[1]/div/div[1]/input').send_keys("Jw4567**")
#Locating By CSS Selector
driver.find_element_by_css_selector("#confirm-passwd > div.aCsJod.oJeWuf > div > div.Xb9hP > input").send_keys("Jw4567**")
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]").click()

time.sleep(3)
# element = driver.find_element_by_xpath('//*[@id="headingText"]/span')

if driver.find_element_by_xpath('//*[@id="headingText"]/span').text == 'Verifying your phone number':
    print("Test Passed and opening Help Link present on the page")
    time.sleep(3)
    #Locating Hyperlinks by Link Testing
    driver.find_element_by_link_text("Help").click()
    time.sleep(5)
    driver.quit()
else:
    print("Test Failed")

# driver.find_element_by_link_text("Help").click()




