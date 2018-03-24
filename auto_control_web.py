
# coding=utf-8
import os
import time
import wx

if __name__ == '__main__':

    app = wx.App()
    window = wx.Frame(None, title = "自动签入签出", size = (400,300))
    panel = wx.Panel(window)
    label = wx.StaticText(panel, label = "腾讯内部自助签到程序", pos = (120,20))
    window.Show(True)
    app.MainLoop()




