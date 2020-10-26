
from selenium import webdriver
import config
import time


driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://vk.com/')

login = driver.find_element_by_id('index_email')
login.send_keys(config.login)

password = driver.find_element_by_id('index_pass')
password.send_keys(config.password)

button = driver.find_element_by_id('index_login_button')
button.click()
#driver.close()


time.sleep(4)
driver.get('https://vk.com/im?sel=137136455')
field = driver.find_element_by_id('im_editable137136455')
field.send_keys('Привет!')