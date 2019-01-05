# coding=utf-8
import logging

#日志模块初识
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='D:\\03F_DISK\\demo2.log', filemode="w",level=logging.INFO, format=LOG_FORMAT)


logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")
