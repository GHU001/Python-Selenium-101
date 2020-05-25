from selenium import webdriver
import time

wd = webdriver.Chrome(r'/Users/guanyanghu/Downloads/chromedriver')
wd.implicitly_wait(5)

wd.get('http://www.google.com/')

time.sleep(10)
element = wd.find_element_by_class_name('gLFyf')
element.send_keys('  \n')
print(element)




