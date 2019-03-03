# !/usr/bin/env python
# -*- coding:utf-8 -*-
# import logging
# import logging.handlers
# import datetime
# '''
# 日志器（logger）是入口，真正干活儿的是处理器（handler），
# 处理器（handler）还可以通过过滤器（filter）和格式器
# （formatter）对要输出的日志内容做过滤和格式化等处理操作。
# '''
#
# logger = logging.getLogger('mylogger')
# logger.setLevel(logging.DEBUG)
#
# rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backupCount=7)
# rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
#
# f_handler = logging.FileHandler('error.log')
# f_handler.setLevel(logging.ERROR)
# f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))
#
# logger.addHandler(rf_handler)
# logger.addHandler(f_handler)
#
# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warning message')
# logger.error('error message')
# logger.critical('critical message')

import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT)

logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")



