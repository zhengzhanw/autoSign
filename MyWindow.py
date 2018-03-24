
from win32api import GetVolumeInformation
from ui.main import Ui_Main
from autoLogin import core
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import time, datetime
import base64
from pyDes import *

class MyWindow(QMainWindow, Ui_Main):
    def __init__(self, name, passwd, qq):
        super(MyWindow,self).__init__()
        self.setupUi(self)

        self.name = name
        self.passwd = passwd
        self.qq = qq

        #self.day1.setTristate(False)
        self.day1.setCheckState(Qt.Checked)
        self.day2.setCheckState(Qt.Checked)
        self.day3.setCheckState(Qt.Checked)
        self.day4.setCheckState(Qt.Checked)
        self.day5.setCheckState(Qt.Checked)
        self.day_list = [1, 2, 3, 4, 5]
        # self.start_time = time.strptime("2017-00-00 08:30:00", "%Y-%m-%d %H:%M:%S")
        # self.end_time = time.strptime("2017-00-00 18:00:00", "%Y-%m-%d %H:%M:%S")
        self.start_time = "08:30:00"
        self.end_time = "18:00:00"
        self.startTime.setTime(QTime(8,30))
        self.endTime.setTime(QTime(18,00))
        self.setWindowIcon(QIcon('myapp.png'))


        self.timer = QTimer(self) #初始化一个定时器
        self.timer.timeout.connect(self.operate) #计时结束调用operate()方法
        #最小化到托盘
        self.tray = QSystemTrayIcon() #创建系统托盘对象
        self.icon = QIcon('myapp.png')  #创建图标
        self.tray.setIcon(self.icon)  #设置系统托盘图标
        self.tray.activated.connect(self.TuoPanEvent) #设置托盘点击事件处理函数
        self.tray_menu = QMenu(QApplication.desktop()) #创建菜单
        self.RestoreAction = QAction(u'还原 ', self, triggered=self.show) #添加一级菜单动作选项(还原主窗口)
        self.QuitAction = QAction(u'退出 ', self, triggered=qApp.quit) #添加一级菜单动作选项(退出程序)
        self.tray_menu.addAction(self.RestoreAction) #为菜单添加动作
        self.tray_menu.addAction(self.QuitAction)
        self.tray.setContextMenu(self.tray_menu) #设置系统托盘菜单
        self.CHECK_IN = False
        self.CHECK_OUT = False


    def TuoPanEvent(self, reason):
        "鼠标点击icon传递的信号会带有一个整形的值，1是表示单击右键，2是双击，3是单击左键，4是用鼠标中键点击"
        if reason == 2 or reason == 3:
            pw = self.parent()
            if pw.isVisible():
                pw.hide()
            else:
                pw.show()
        print(reason)

    def operate(self):
        week = time.localtime()
        week = int(time.strftime("%w", week))
        if week in self.day_list:
            current = datetime.datetime.now().strftime('%H:%M:%S')
            #print ("2017-01-01 " +current)
            current = time.strptime("2017-01-01 " + current, "%Y-%m-%d %H:%M:%S")
            current_date = time.mktime(current)
            start_date = time.mktime(time.strptime("2017-01-01 " + self.start_time, "%Y-%m-%d %H:%M:%S"))
            end_date = time.mktime(time.strptime("2017-01-01 " + self.end_time, "%Y-%m-%d %H:%M:%S"))
            print(current_date)
            print(start_date)
            print(end_date)
            if abs(current_date - start_date) <= 30 and self.CHECK_IN == False:
                content = core.signed_oa(self.name, self.passwd, 0)
                to_who = self.qq
                msg = content
                core.send_qq(to_who, msg)
                self.CHECK_IN = True
                self.CHECK_OUT = False
            if abs(current_date - end_date) <= 30 and self.CHECK_OUT == False:
                content = core.signed_oa(self.name, self.passwd, 1)
                to_who = self.qq
                msg = content
                core.send_qq(to_who, msg)
                self.CHECK_IN = False
                self.CHECK_OUT = True


    def on_startTask_click(self):
        self.timer.start(1000*60) #设置计时间隔并启动
        self.startTask.setEnabled(False)
        print("定时任务已执行")

    def on_checkIn_click(self):
        content = core.signed_oa(self.name, self.passwd, 0)
        to_who = self.qq
        core.send_qq(to_who, content)

    def on_checkOut_click(self):
        content = core.signed_oa(self.name, self.passwd, 1)
        to_who = self.qq
        core.send_qq(to_who, content)

    def on_startTime_click(self):
        self.start_time = self.startTime.time().toString()
        print(self.start_time)

    def on_endTime_click(self):
        self.end_time = self.endTime.time().toString()
        print(self.end_time)

    def on_day1_click(self, state):
        if state:
            if 1 not in self.day_list:
                self.day_list.append(1)
        else:
            if 1 in self.day_list:
                self.day_list.remove(1)
    def on_day2_click(self, state):
        if state:
            if 2 not in self.day_list:
                self.day_list.append(2)
        else:
            if 2 in self.day_list:
                self.day_list.remove(2)
    def on_day3_click(self, state):
        if state:
            if 3 not in self.day_list:
                self.day_list.append(3)
        else:
            if 3 in self.day_list:
                self.day_list.remove(3)
    def on_day4_click(self, state):
        if state:
            if 4 not in self.day_list:
                self.day_list.append(4)
        else:
            if 4 in self.day_list:
                self.day_list.remove(4)
    def on_day5_click(self, state):
        if state:
            if 5 not in self.day_list:
                self.day_list.append(5)
        else:
            if 5 in self.day_list:
                self.day_list.remove(5)
    def on_day6_click(self, state):
        if state:
            if 6 not in self.day_list:
                self.day_list.append(6)
        else:
            if 6 in self.day_list:
                self.day_list.remove(6)
    def on_day7_click(self, state):
        if state:
            if 0 not in self.day_list:
                self.day_list.append(0)
        else:
            if 0 in self.day_list:
                self.day_list.remove(0)

    def message_box(self,title,context):
        QMessageBox.information(self, title, context)

def DesEncrypt(str):
    Des_Key = "BHC#@*UM" # Key
    Des_IV = b"\0\0\0\0\0\0\0\0" # 自定IV向量
    k = des(Des_Key, CBC, Des_IV, pad=None, padmode=PAD_PKCS5)

    EncryptStr = k.encrypt(str)

    return base64.b64encode(EncryptStr) #转base64编码返回

def line_to_tuple(line):
    parts = line.strip().split("=")
    return (parts[0], parts[1])

if __name__ == '__main__':
    map_user = dict()
    for row in open("config.ini", 'rb').readlines():
        if row == "":
            continue
        parts = line_to_tuple(str(row, encoding="utf-8"))
        map_user[parts[0]] = parts[1]

    app = QApplication(sys.argv)
    import ctypes
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
    window = MyWindow(map_user["name"], map_user["passwd"], map_user["QQ"])
    window.show()

    if "Code" in map_user:
        tuple = GetVolumeInformation("c:\\")
        machine_code = ""
        for em in tuple[1:-1]:
            machine_code += str(em)
        register_code = DesEncrypt(machine_code)
        register_code = str(register_code, encoding="utf-8")
        print(register_code)
        if register_code != map_user.get("Code"):
            window.message_box("Warning", "注册码不正确")
            sys.exit()

    else:
        window.message_box("Warning", "请配置注册码")
        sys.exit()
    #window.tray.show()

    sys.exit(app.exec_())