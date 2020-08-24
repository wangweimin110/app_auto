# -*- coding: utf-8 -*- 
"""
    @Author WWM
    @Date 2020/8/19 22:22
"""
import logging
from Common.config_path import *


class MyLog:

    def my_log(self, msg, level):

        my_logger = logging.getLogger('APP')
        my_logger.setLevel('DEBUG')
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息：%(message)s')
        sh = logging.StreamHandler()
        sh.setLevel('DEBUG')
        sh.setFormatter(formatter)
        fh = logging.FileHandler(log_path, encoding='utf-8')
        fh.setLevel('DEBUG')
        fh.setFormatter(formatter)
        my_logger.addHandler(sh)
        my_logger.addHandler(fh)
        if level == 'DEBUG':
            my_logger.debug(msg)
        elif level == 'INFO':
            my_logger.info(msg)
        elif level == 'WARNING':
            my_logger.warning(msg)
        elif level == 'ERROR':
            my_logger.error(msg)
        elif level == 'CRITICAL':
            my_logger.critical(msg)
        my_logger.removeHandler(sh)
        my_logger.removeHandler(fh)

    def debug(self, msg):
        self.my_log(msg, 'DEBUG')

    def info(self,msg):
        self.my_log(msg,'INFO')

    def warning(self,msg):
        self.my_log(msg,'WARNING')

    def error(self,msg):
        self.my_log(msg,'ERROR')

    def critical(self,msg):
        self.my_log(msg,'CRITICAL')


if __name__ == '__main__':

    my_logger = MyLog().debug('LALALA')
