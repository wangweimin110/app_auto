# -*- coding: utf-8 -*- 
"""
    @Author WWM
    @Date 2020/8/19 22:23
"""

import os

project_path = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

# 日志路径
log_path = os.path.join(project_path, 'OutPuts', 'Logs', 'log_app.txt')
# 截图路径
screenshot_path = os.path.join(project_path, 'OutPuts', 'Screenshots')
# 报告路径
report_path = os.path.join(project_path, 'OutPut', 'Reports')
