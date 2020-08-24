# -*- coding: utf-8 -*- 
"""
    @Author WWM
    @Date 2020/8/15 1:28
"""

# UI Automator
'''
UI自动化测试框架，安卓移动端app
提供了一系列API：执行UI测试在系统或者第三方APP上面
允许在被测设备上执行操作，比如打开系统设置菜单
适合编写黑盒自动化测试
UI Automator框架的主要特点：
    元素定位：UI Automator Viewer  扫描、分析待测应用的UI组件的图像工具
    元素操作：Accessing device state 在目标设备和APP上的各种操作
    元素识别：UI Automator APIs 在多个应用程序中捕获和操作UI组件
app元素定位
    id:resrouce-id   driver.find_element_by_id()
    ClassName:class  driver.find_element_by_class_name()
    AccessibilityId:content-desc   driver.find_element_by_accessibility_id()
    AndroidUiAutomator: driver.find_element_by_android_uiautomator()
        UiSelector找元素  new ui = UiSelector()/new UiSelector() new实例化
        new UiSelector().resourceId("com.chineseall.reader:id/tv_login").text("登录")
        new UiSelector().text()/new UiSelector().description() 全部匹配    description -根据content-desc匹配
        new UiSelector().textContains()/new UiSelector().descriptionContains() 部分匹配
        new UiSelector().textMatches()/new UiSelector().descriptionMatches() 正则匹配
        new UiSelector().textStartWith()/new UiSelector().descriptionStartWith() 以**开头匹配
        例：
        WebDriverWait(driver,10).until(ec.visibility_of_element_located((MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("下一步")')))
        driver.find_element_by_android_uiautomator('new UiSelector().text("下一步")').click()
        WebDriverWait(driver,10).until((lambda x: x.find_element_by_android_uiautomator('new UiSelector().text("我的")')))
        driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        WebDriverWait(driver,10).until((lambda x: x.find_element_by_android_uiautomator('new UiSelector().text("我的设置")')))
        driver.find_element_by_android_uiautomator('new UiSelector().text("我的设置")').click()
        WebDriverWait(driver,10).until((lambda x: x.find_element_by_android_uiautomator('new UiSelector().text("切换账户")')))
        driver.find_element_by_android_uiautomator('new UiSelector().text("切换账户")').click()
'''

# appium 滑动操作
'''
原理：
    1、先获取设备的屏幕大小（长、宽）
    2、在设置滑动的距离与屏幕大小的百分比
    2、调用滑动接口执行滑动操作
获取当前窗口大小：
    get_window_size   返回窗口的宽、高
滑动接口：   
    swipe(起始X,起始Y,结束X,结束Y)
例：
    size = driver.get_window_size()

    start_x = size['width'] * 0.9
    start_y = size['height'] * 0.5
    end_x = size['width'] * 0.1
    end_y = size['height'] * 0.5
    # 从右向左滑动
    driver.swipe(start_x, start_y, end_x, end_y, 200)
    time.sleep(1)
    # 从左向右滑动
    driver.swipe(end_x, end_y, start_x, start_y, 200)
    
    start_x_1 = size['width'] * 0.5
    start_y_1 = size['height'] * 0.9
    end_x_1 = size['width'] * 0.5
    end_y_1 = size['height'] * 0.1
    # 从下往上滑动
    driver.swipe(start_x_1, start_y_1, end_x_1, end_y_1, 200)
    time.sleep(1)
    # 从上往下滑动
    driver.swipe(end_x_1, end_y_1, start_x_1, start_y_1, 200)
'''

# 触屏操作
'''
TouchAction类
将一系列的动作放在一个链条中，然后将该链条传递给服务器，服务器收到该链条后，解析个动作，逐个执行
短按（press）
长按（longPress）
点击（tap)
移动到（move_to） x,y为相对上一个坐标的移动距离
等待（wait）
释放（release）
执行（perform）
取消（cancel）
九宫格为例:
    from appium.webdriver.common.touch_action import TouchAction
    # 元素定位
    ele = driver.find_element_by_id('')
    # 元素的大小
    size = ele.size
    # 均分的步长  宽高一样
    step = size['width']/6
    # 起点坐标
    spc = ele.location
    # 触摸位置
    point_1 = (spc['x'] + step, spc['y'] + step)
    point_2 = (point_1[0] + step*2, point_1[1])
    point_3 = (point_2[0] + step*2, point_2[1])
    point_4 = (point_3[0] - step*2, point_3[1] + step*2)
    point_5 = (point_4[0], point_4[1] + step*2)
    
    TouchAction(driver).press(x=point_1[0], y=point_1[1]).wait(200).move_to(x=point_2[0], y=point_2[1]).\
                        move_to(x=point_3[0], y=point_3[1]).\
                        move_to(x=point_4[0], y=point_4[1]).\
                        move_to(x=point_5[0], y=point_5[1]).\
                        release().perform()

TouchActions类的方法
方法：tap(on_element) 点击给定元素
Taps on a given element 单击
方法：double_tap(on_element) 双击特定元素
Double taps on a given element 双击
方法：tap_and_hold(xcoord, ycoord)
Touch down at given coordinates 在给定坐标处按住
方法：move(xcoord, ycoord) 在屏幕上执行手势“移动”
Move held tap to specified location 将保持点击移动到指定位置
方法：scroll(xoffset, yoffset) 滚动到某个位置(按x和y偏移滚动)
Touch and scroll, moving by xoffset and yoffset
触摸并滚动，按xoffset和yoffset移动
方法：scroll_from_element(on_element, xoffset, yoffset) 从某元素开始滚动到某个位置
Touch and scroll starting at on_element, moving by xoffset and yoffset
从on_element开始触摸并滚动，按xoffset和yoffset移动
方法：long_press(on_element)
Long press on an element 长按一个元素
方法：flick(xspeed, yspeed)
Flicks, starting anywhere on the screen 轻弹，从屏幕上的任何位置开始
方法：flick_element(on_element, xoffset, yoffset, speed) 从某元素开始以指定的速度移动(执行轻弹手势)
Flick starting at on_element, and moving by the xoffset and yoffset with specified speed
从on_element开始轻弹，然后按xoffset和yoffset移动以指定的速度
release() perform()
九宫格为例:
    from selenium.webdriver.common.touch_actions import TouchActions
    # 元素定位
    ele = driver.find_element_by_id('')
    # 元素的大小
    size = ele.size
    # 均分的步长  宽高一样
    step = size['width']/6
    # 起点坐标
    spc = ele.location
    # 触摸位置
    point_1 = (spc['x'] + step, spc['y'] + step)
    point_2 = (point_1[0] + step*2, point_1[1])
    point_3 = (point_2[0] + step*2, point_2[1])
    point_4 = (point_3[0] - step*2, point_3[1] + step*2)
    point_5 = (point_4[0], point_4[1] + step*2)
    
    TouchActions(driver).tap_and_hold(point_1[0], point_1[1]).move(point_2[0], point_2[1]).\
                        move(point_3[0], point_3[1]).move(point_4[0], point_4[1]).\
                        move(point_5[0], point_5[1]).release(point_5[0], point_5[1]).perform()
'''

# Toast提示信息获取
'''
要求：
    1、appium server版本1.63+以上
    2、代码中必须指定automationName为：UiAutomator2
    3、UiAutomator2只支持安卓5.0+版本
    4、要求安装jdk1.8 64位以上 配置其环境变量
toast_loc=(MobileBy.XPATH,".//*[contains(@text,'再按一次返回键退出淘宝')]")
# 等待时要用presence_of_all_elements_located  不能用visibility_of_element_located 会报错
WebDriverWait(driver,10,0.1).until(ec.presence_of_all_elements_located(toast_loc))
print(driver.find_element_by_xpath(".//*[contains(@text,'再按一次返回键退出淘宝')]").text)
'''

# 混合应用-H5
'''
hybird混合应用自动化方案
基于UiAutomator+Chromedriver
native(原生)部分走UiAutomator，webview部分走Chromedriver，二者结合
webview必须为debug版本

获取webview页面的三种方式：
    1、Chrome://inspect,需要FQ
    2、使用driver.page_source获取HTML页面
    3、找开发人员要源文件
    4、uc-devtools 不需要FQ
上下文切换：
列出可用的上下文（Context）
driver.contexts

driver.window.handles
当前上下文（context）
driver.current_context

切换至默认的上下文（context）  一般就是原生上下文 'native_app'
driver.switch_to.context(None)

获取当前Activity 仅支持安卓
driver.current_activity

获取当前包名： 仅支持安卓
driver.current_package  

例：
loc = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("")')
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
driver.find_element_by_android_uiautomator('new UiSelector().text("")').click()

# 等待WebView元素出现
WebDriverWait(driver, 20).until(ec.visibility_of_element_located((MobileBy.CLASS_NAME, 'android.webkit.WebView')))
time.sleep(1)

# 前提 代码可以识别到WebView  需开启app的webview debug属性
# 列出所有的context
cons = driver.contexts  # 列表
print(cons)

# 切换至webview  要确保Chromedriver的版本匹配
driver.switch_to.context(cons[-1])

# 切换完成后 到HTML页面 等待元素出现   uc-devtools识别HTML页面 定位元素
WebDriverWait(driver, 20).until(ec.visibility_of_element_located((MobileBy.XPATH, '')))
driver.find_element_by_xpath('').click()

'''


# 微信小程序测试
'''
我的博客用户名：WangWeimin110  密码：qqqq1111
打开任意对话框 输入debugx5.qq.com 点击
参考https://www.cnblogs.com/yyoba/p/9455519.html
'''

# Yaml
'''
Yaml是一种简洁的非标记语言
Yaml以数据为中心，使用空白，缩进，分行组织数据，从而使得表示更加简洁
基本规则：
    1、大小写敏感
    2、使用缩进表示层级关系
    3、禁止使用tab缩进，只能使用空格键
    4、缩进长度没有限制，只要元素对齐就表示这些元素属于一个层级
    5、用#表示注释
    6、字符串可以不用''标注
三种数据结构：
    1、字典
        使用冒号（:）表示键值对，同一缩进的所有键值对属于一个map
        方式一(注意冒号后面的空格)：
            platformName: Android
            platformVersion: 7.1
        方式二：
            {platformName:Android,platformVersion:7.1}
    2、列表
        使用连字符（-）表示，注意-后面的空格
        方式一：
            - hello
            - world
        方式二：
            [hello,world,12,13]
    3、scalar,纯量
PyYAML安装：pip install PyYaml
引入：import yaml
读取yaml文件的数据，转换成python对象
    1、打开yaml文件
    2、使用yaml的load()函数
    例：fs = open(os.path.join(caps_dir,'caps.yaml'))
        datas = yaml.load(fs)
'''