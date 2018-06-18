# -*- coding: UTF-8-*- #
from selenium import webdriver
from selenium.webdriver.support.ui import Select

    #打开Firefox
driver = webdriver.Firefox()
    #打开网页延迟10s
driver.implicitly_wait(10)

    #搜索找到12306网站
driver.get('https://kyfw.12306.cn/otn/leftTicket/init')
    #找到出发地id地址
fromEle = driver.find_element_by_id('fromStationText')
    #点击清空一下
fromEle.click()
fromEle.clear()
    #输入要搜索的地址
fromlocation = '北京\n'
fromlocation = unicode(fromlocation,"UTF-8")
fromEle.send_keys(fromlocation)

    #找到到达地id地址
toEle = driver.find_element_by_id('toStationText')
    #点击清空一下
toEle.click()
toEle.clear()
    #输入要搜索的地址
tolocation = '葫芦岛北\n'
tolocation = unicode(tolocation,"UTF-8")
toEle.send_keys(tolocation)

     #找到查询按钮并且进行点击
search = driver.find_element_by_id('query_ticket')
search.click()
     #找到时间选择框，选择时间区间
timeSelect = Select(driver.find_element_by_id('cc_start_time'))
timeSelect.select_by_visible_text('12:00--18:00')

xpath = '//*[@id="quertLeftTable"]//td[4][@class]/../td[1]//a'

theTrains = driver.find_element_by_xpath(xpath)
for one in theTrains:
    print (one.text)

driver.quit()




