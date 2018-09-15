from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
import time


url = 'http://www.bilibili.com'
account = '账号'
pwd = '密码'
login_text = '登录'
login_user = 'login_username'
login_pwd = 'login_passwd'
login_button = 'btn btn_login'
d = webdriver.Chrome()

def openurl(handle,url):

    handle.get(url)

def findElement(d,arg):

    login_window = d.find_element_by_class_name(arg['login_window'])
    ActionChains(d).move_to_element(login_window)

    ele1 =  d.find_element_by_link_text(arg['text_id'])
    ele1.click()

    use_id = d.find_element_by_id(arg['use_id'])
    pwd_id = d.find_element_by_id(arg['pwd_id'])
    login_button = d.find_element_by_link_text(arg['login_button'])
    return use_id,pwd_id,login_button

def sendVals(eletuple,arg):
    listkey = ['username','password']
    i = 0
    for key in listkey:
        eletuple[i].send_keys(' ')
        eletuple[i].clear()
        eletuple[i].send_keys(arg[key])
        i+=1
    eletuple[2].click()

def get_distance(image1, image2):
    '''
    拿到滑动验证码需要移动的距离
    :param image1:没有缺口的图片对象
    :param image2:带缺口的图片对象
    :return:需要移动的距离
    '''
    threshold = 60
    left = 57
    for i in range(left, image1.size[0]):
        for j in range(image1.size[1]):
            rgb1 = image1.load()[i, j]
            rgb2 = image2.load()[i, j]
            res1 = abs(rgb1[0] - rgb2[0])
            res2 = abs(rgb1[1] - rgb2[1])
            res3 = abs(rgb1[2] - rgb2[2])
            if not (res1 < threshold and res2 < threshold and res3 < threshold):
                return i - 7  # 经过测试，误差为大概为7

    return i - 7  # 经过测试，误差为大概为7

def get_tracks(distance):
    '''
    拿到移动轨迹，模仿人的滑动行为，先匀加速后匀减速
    匀变速运动基本公式：
    ①v=v0+at
    ②s=v0t+½at²
    ③v²-v0²=2as
    :param distance: 需要移动的距离
    :return: 存放每0.3秒移动的距离
    '''
    # 初速度
    v = 0
    # 单位时间为0.2s来统计轨迹，轨迹即0.2内的位移
    t = 0.3
    # 位移/轨迹列表，列表内的一个元素代表0.2s的位移
    tracks = []
    # 当前的位移
    current = 0
    # 到达mid值开始减速
    mid = distance * 4 / 5

    while current < distance:
        if current < mid:
            # 加速度越小，单位时间的位移越小,模拟的轨迹就越多越详细
            a = 2
        else:
            a = -3

        # 初速度
        v0 = v
        # 0.2秒时间内的位移
        s = v0 * t + 0.5 * a * (t ** 2)
        # 当前的位置
        current += s
        # 添加到轨迹列表
        tracks.append(round(s))

        # 速度已经达到v,该速度作为下次的初速度
        v = v0 + a * t
    return tracks

def move_slider(tracks,):
    slider = d.find_element_by_xpath('//div[@id="gc-box"]/div/div[3]/div[2]')
    ActionChains(d).click_and_hold(slider).perform()
    for track in tracks:
        ActionChains(d).move_by_offset(xoffset=track, yoffset=0).perform()
    else:
        ActionChains(d).move_by_offset(xoffset=3, yoffset=0).perform()  # 先移过一点
        ActionChains(d).move_by_offset(xoffset=-3, yoffset=0).perform()  # 再退回来，是不是更像人了

    time.sleep(0.5)  # 0.5秒后释放鼠标
    ActionChains(d).release().perform()

def login_test():

    openurl(d,url)
    d.maximize_window()

    ele_dict = {'login_window':'face',
                'text_id':'登录',
                'use_id':'login-username',
                'pwd_id':'login-passwd',
                'login_button':'登录'}

    account_dict = {'username':account, 'password':pwd}
    ele_tupe = findElement(d,ele_dict)
    sendVals(ele_tupe,account_dict)

if __name__ == '__main__':
    try:
        login_test()
        d.save_screenshot('lodin.png')
        # 获取滑块
        slider = d.find_element_by_xpath('//div[@id="gc-box"]/div/div[3]/div[2]')
        print(slider)
        # 鼠标悬停事件(显示完整图片)
        ActionChains(d).move_to_element(slider).perform()
        time.sleep(1)
        screenshot = d.save_screenshot('tu1.png')

        print(type(screenshot))

        time.sleep(2)

        # 鼠标点击(显示残缺图片)
        slider.click()
        time.sleep(3)
        d.save_screenshot('tu2.png')

        # 获取 图片的位置大小
        img1 = d.find_element_by_xpath(xpath='//div[@class="gt_cut_fullbg gt_show"]')
        location = img1.location
        size = img1.size
        top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
               'width']
        print('图片的宽:', img1.size['width'])
        print(top, bottom, left, right)

        #  保存 裁剪 图片
        img_1 = Image.open('tu1.png')
        img_2 = Image.open('tu2.png')
        capcha1 = img_1.crop((left, top, right, bottom))
        capcha2 = img_2.crop((left, top, right, bottom))
        capcha1.save('tu1-1.png')
        capcha2.save('tu2-2.png')

        # 获取验证码图片
        img_11 = Image.open('tu1-1.png')
        img_22 = Image.open('tu2-2.png')

        distance = get_distance(img_11, img_22)

        tracks = get_tracks(distance)
        print(tracks)
        print(distance, sum(tracks))
        move_slider(tracks)
    except:
        pass







































































































































































