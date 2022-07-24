import logging


from logging.handlers import TimedRotatingFileHandler
import sys
import os
from regression_model.config import config

FORMATTER  = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname) s -"
    "%(funcName)s:%(lineno)d - %(message)s")

LOG_FILE = config.LOG_DIR / 'ml_models.log'

def get_console_handler():

    console_handler = logging.StreamHandler(sys.stdout)

    console_handler.setFormatter(FORMATTER)

    return console_handler

def get_file_handler():
    isExist = os.path.exists(config.LOG_DIR)
    if (not isExist):
        os.makedirs(config.LOG_DIR)

    #print("Error here lol")
    file_handler = TimedRotatingFileHandler(LOG_FILE, when ='midnight')

    file_handler.setFormatter(FORMATTER)

    file_handler.setLevel(logging.WARNING)

    return file_handler

def get_logger(logger_name):
    isExist = os.path.exists(config.LOG_DIR)
    if (not isExist):
        os.makedirs(config.LOG_DIR)
    logger = logging.getLogger(logger_name)

    logger.setLevel(logging.DEBUG)

    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())

    logger.propagate = False

    return logger


