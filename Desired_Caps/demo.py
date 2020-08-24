# -*- coding: utf-8 -*- 
"""
    @Author WWM
    @Date 2020/8/9 17:20
"""

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from appium.webdriver.common.touch_action import TouchAction
import time
import yaml


# 打开yaml文件
fs = open('caps.yaml')
# 转换成python对象
res = yaml.load(fs)
print(res)

'''
获取应用包名和入口activity
    aapt目录：sdk/build-tools/aapt
    命令语法：aapt dump badging apk应用名
        例：aapt dump badging 路径\直销银行.apk
'''
# desired_caps = {
#                 # 测试的设备
#                 'platformName': 'Android',
#                 # 手机设备名称，通过adb devices查看
#                 'deviceName': 'Android Emulator',
#                 # 手机设备的系统版本号
#                 'platformVersion': '7.1',
#                 'automationName': 'UiAutomator1',
#                 # 'newCommandTimeout': "3000",
#                 # apk包名
#                 'appPackage': 'com.chineseall.reader',
#                 # APP入口 Acitivity
#                 'appActivity': 'com.chineseall.reader.ui.activity.SplashActivity',
#                 # 启动app时不要清除app里的原有的数据
#                 'noReset': True
#                 }

# 连接appium server 前提：appium desktop要启动 有监听端口
# 将我们的服务器参数(desired_caps)传递给appium server  打开app
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

# 运行代码之前：1、appium server启动成功，处于监听状态
# 2、模拟器/真机必须能够被电脑识别，即adb devices能够识别到要操作的设备



