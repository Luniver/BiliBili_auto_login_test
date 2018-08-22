#_*_ coding:UTF-8_*_#
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import numpy as np
import math

def get_ele_time(driver,times,func):
    return WebDriverWait(driver,times).until(func)

def ease_out_expo(x):
    if x == 1:
        return 1
    else:
        return 1 - pow(2, -10 * x)

def get_tracks(distance, seconds, ease_func):
    tracks = [0]
    offsets = [0]

    for t in np.arange(0.0, seconds, 0.1):
        ease = globals()[ease_func]
        offset = round(ease(t / seconds) * distance)
        tracks.append(offset - offsets[-1])
        offsets.append(offset)
        return offsets, tracks


def drag(browser, offset):
    button = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[3]/div/div/ul/li[3]/div/div/div[3]/div[2]')
    offsets, tracks = easing.get_tracks(offset, 12, 'ease_out_expo')
    ActionChains(browser).click_and_hold(button).perform()
    for x in tracks:
        ActionChains(browser).move_by_offset(x, 0).perform()
        ActionChains(browser).pause(0.5).release().perform()

def openBrowser():
    driver = webdriver.Firefox()
    return driver
def openurl(handle,url):
    handle.get(url)
    driver.maximize_window()
    time.sleep(2)
def login_test():

    ele = driver.find_element_by_class_name('face')
    ActionChains(driver).move_to_element(ele)

    #ele1 = driver.find_element_by_class_name('login-btn')
    ele1 = get_ele_time(driver,10,lambda d:driver.find_element_by_class_name('login-btn'))
    ele1.click()

    username = driver.find_element_by_id('login-username')
    username.clear()
    username.send_keys('13985418586')
    time.sleep(2)

    password = driver.find_element_by_id('login-passwd')
    password.clear()
    password.send_keys('520z722j725mlcy')
    time.sleep(2)

    drag(driver,0)
    time.sleep(2)

    login = driver.find_element_by_class_name('btn btn-login')
    login.click()
    time.sleep(2)



