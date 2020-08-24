# -*- coding: utf-8 -*- 
"""
    @Author WWM
    @Date 2020/8/19 22:23
"""
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Common.my_log import MyLog


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # 向上滑动
    def swipe_up(self):
        pass

    # 向下滑动
    def swipe_down(self):
        pass

    # 向左滑动
    def swipe_left(self, size):
        # 从右向左滑动
        self.driver.swipe(size['width'] * 0.9, size['height'] * 0.5, size['width'] * 0.1, size['height'] * 0.5, 200)

    # 向右滑动
    def swipe_right(self):
        pass

    # 获取整个屏幕大小
    def get_size(self):
        return self.driver.get_window_size()

    # toast获取
    def get_toast_msg(self, text):
        toast_loc = "//*[contains(@text,'{}]')]".format(text)
        # 等待时要用presence_of_all_elements_located  不能用visibility_of_element_located 会报错
        try:
            WebDriverWait(self.driver, 10, 0.1).until(ec.presence_of_all_elements_located((MobileBy.XPATH, toast_loc)))
            return self.driver.find_element_by_xpath(toast_loc).text
        except:
            MyLog().error('没有找到匹配的toast！')
    # H5 切换
