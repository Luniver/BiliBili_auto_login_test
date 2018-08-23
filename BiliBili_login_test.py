#_*_ coding:UTF-8_*_#
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time
import numpy as np

url = 'http://www.bilibili.com'
account = '13985418586'
pwd = '520z722j725mlcy'
login_text = '登录'
login_user = 'login_username'
login_pwd = 'login_passwd'
login_button = 'btn btn_login'


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
    time.sleep(2)

def findElement(d,arg):

    login_window = d.find_element_by_class_name(arg['login_window'])
    ActionChains(d).move_to_element(login_window)

    ele1 =  d.find_element_by_link_text(arg['text_id'])
    ele1.click()

    user_id = d.find_element_by_id(arg[id='user_id'])
    pwd_id = d.find_element_by_id(arg[id='pwd_id'])
    login_button = d.find_element_by_class_name(arg['login_button'])
    return user_id,pwd_id,login_button

def sendVals(eletuple,arg):
    listkey = ['username','password']
    i = 0
    for key in listkey:
        eletuple[i].send_keys(' ')
        eletuple[i].clear()
        eletuple[i].send_keys(arg[key])
        i+=1
    eletuple[2].click()


def login_test():
    d = openBrowser()
    openurl(d,url)
    d.maximize_window()

    ele_dict = {'login_window':'face',
                'text_id':login_text,
                'user_id':login_user,
                'pwd_id':login_pwd,
                'login_button':login_button}

    account_dict = {'username': account, 'password': pwd}
    ele_tupe = findElement(d, ele_dict)
    sendVals(ele_tupe,account_dict)


    drag(driver,0)
    time.sleep(2)


    login.click()
    time.sleep(2)

if __name__ == '__main__':
    login_test()



