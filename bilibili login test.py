# -*- coding: UTF-8-*- #
from selenium import webdriver
driver = webdriver.Firefox()
driver.get('http://www.bilibili.com')
element_search_button = driver.find_element_by_class_name("face")
element_search_button.click()
element_keyword = driver.find_element_by_id("login-username")
element_change = '13985418586'
element_change = unicode(element_change,"utf-8")
element_keyword.send_keys(element_change)
element_keyword = driver.find_element_by_id("login-passwd")
element_change = '520z722j725mlcy'
element_change = unicode(element_change,"utf-8")
element_keyword.send_keys(element_change)

element_click = driver.find_element_by_class_name("btn btn-login")
element_click.click()



