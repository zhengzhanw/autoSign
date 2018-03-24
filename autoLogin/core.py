
# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import win32gui
import win32con
import win32clipboard as w
import pymouse,pykeyboard,os,sys
from pymouse import *
from pykeyboard import PyKeyboard
#from PIL import Image

def getText():
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_UNICODETEXT)
    w.CloseClipboard()
    return d

def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    w.CloseClipboard()

def send_qq(to_who, msg):
    """发送qq消息
    to_who：qq消息接收人
    msg：需要发送的消息
    """
    # 将消息写到剪贴板
    setText(msg)
    # 获取qq窗口句柄
    qq = win32gui.FindWindow(None, to_who)
    # 投递剪贴板消息到QQ窗体
    win32gui.SendMessage(qq, 258, 22, 2080193)
    win32gui.SendMessage(qq, 770, 0, 0)
    # 模拟按下回车键
    win32gui.SendMessage(qq, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    win32gui.SendMessage(qq, win32con.WM_KEYUP, win32con.VK_RETURN, 0)


def signed_oa(name, passwd, check_state=-1):
    content = ""
    try:
        driver = webdriver.Chrome()
        driver.get("http://-----------------------------------")
        driver.find_element_by_id("username").send_keys(name)
        driver.find_element_by_id("password_input").send_keys(passwd)
        print(driver.find_element_by_id("username"))
        print(driver.find_element_by_id("password_input").text)
        driver.find_element_by_id("login_button").click()
        print("登陆成功")
        content += "登陆成功"

        driver.implicitly_wait(30)
        if check_state == 1:
            check_out_btn = driver.find_element_by_id("checkout_btn")
            check_out = check_out_btn.text
            print(check_out)
            if check_out == '签 出':
                check_out_btn.click()
                #driver.find_element_by_name("check").click()
                content += "开始签出...\n"
                print("开始签出。。。")
                driver.implicitly_wait(30)
                # code_input = driver.find_element_by_id("code_input")
                # shootcut = driver.find_element_by_id("image")
                # driver.save_screenshot(r'code.png')
                # left = shootcut.location['x']
                # top = shootcut.location['y']
                # elementWidth = shootcut.location['x'] + shootcut.size['width']
                # elementHeight = shootcut.location['y'] + shootcut.size['height']
                # picture = Image.open(r'code.png')
                # picture = picture.crop((left, top, elementWidth, elementHeight))
                # picture.save(r'E:\photo2.png')
                #confirm = driver.find_element_by_css_selector("a[name=\"check\"]")
                confirm = driver.find_element_by_css_selector("a[name=\"check\"]")
                time.sleep(5)
                confirm.click()
                driver.implicitly_wait(30)
                driver.save_screenshot(r'../code.png')
                table = driver.find_element_by_id("check_in_tbl")
                content += table.text
                #driver.execute_script('document.getElementById(\'tdialog-buttonwrap\').children[0].focus()')
                # print(driver.get_window_position())
                # print(driver.get_window_rect())
                # print(driver.get_window_size())
                # actions = ActionChains(driver)
                # actions.move_to_element(confirm)
                # actions.key_down(Keys.ENTER)
                # actions.perform()
                #confirm.send_keys(Keys.ENTER)

                # k = PyKeyboard()
                # k.press_key(k.enter_key)
                # k.release_key(k.enter_key)
                # ActionChains(driver).move_to_element(confirm).perform()

                #content += "签出成功"
        elif check_state == 0:
            check_out_btn = driver.find_element_by_id("checkin_btn")
            check_out = check_out_btn.text
            print(check_out)
            if check_out == '马上签入':
                check_out_btn.click()
                content += "开始签入..."
                driver.implicitly_wait(30)
                confirm = driver.find_element_by_css_selector("a[name=\"check\"]")
                time.sleep(5)
                confirm.click()
                driver.implicitly_wait(30)
                driver.save_screenshot(r'../code.png')
                table = driver.find_element_by_id("check_in_tbl")
                content += table.text
                #content += "签入成功"

    except Exception as e:
        print (e)
        content = content + "\n\n\nException is: %s" % e

    return content


if __name__ == '__main__':

    #content = signed_oa(1)
    # 测试
    to_who = ''
    msg = "测试！！！"
    send_qq(to_who, msg)
