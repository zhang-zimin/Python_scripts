from selenium import webdriver
import yagmail
import time
import os

webdriver = webdriver.Chrome(r'C:\Program Files\Python39\chromedriver.exe')
webdriver.get(
    r"http://ids.hhu.edu.cn/amserver/UI/Login?goto=http://form.hhu.edu.cn/pdc/form/list"
)

element = webdriver.find_element_by_id("IDToken1")
element.send_keys("191309070003")

element = webdriver.find_element_by_id("IDToken2")
element.send_keys("zhang19961029")

webdriver.find_element_by_css_selector('img[style="CURSOR: pointer"]').click()
time.sleep(1)
webdriver.find_element_by_class_name("datav-ren-arrow").click()
time.sleep(1)
webdriver.find_element_by_id("saveBtn").click()
time.sleep(1)
