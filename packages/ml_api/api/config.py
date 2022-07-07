import logging

from logging.handlers import TimedRotatingFileHandler
import sys
import os
import pathlib

PACKAGE_ROOT = pathlib.Path(__file__).resolve().parent.parent

FORMATTER  = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname) s -"
    "%(funcName)s:%(lineno)d - %(message)s")

LOG_DIR = PACKAGE_ROOT / 'logs'

LOG_FILE = LOG_DIR / 'ml_api.log'

def get_console_handler():

    console_handler = logging.StreamHandler(sys.stdout)

    console_handler.setFormatter(FORMATTER)

    return console_handler

def get_file_handler():
    isExist = os.path.exists(LOG_DIR)
    if (not isExist):
        os.makedirs(LOG_DIR)

    #print("Error here lol")
    file_handler = TimedRotatingFileHandler(LOG_FILE, when ='midnight')

    file_handler.setFormatter(FORMATTER)

    file_handler.setLevel(logging.INFO)

    return file_handler

def get_logger(logger_name):
    isExist = os.path.exists(LOG_DIR)
    if (not isExist):
        os.makedirs(LOG_DIR)
    logger = logging.getLogger(logger_name)

    logger.setLevel(logging.DEBUG)

    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())

    logger.propagate = False

    return logger

class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'TOP-SECERT'
    SERVER_PORT = 5000

class ProductionConfig(Config):
    DEBUG =  False
    SERVER_PORT = os.environ.get('PORT', 5000)

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

    