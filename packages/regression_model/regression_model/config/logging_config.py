import logging
from logging.handlers import TimedRotatingFileHandler
<<<<<<< HEAD
import os
=======
>>>>>>> 6162c318b58b225e0061fccd6c64cd67fe205c1b
import sys

from regression_model.config import config

# Multiple calls to logging.getLogger('someLogger') return a
# reference to the same logger object.  This is true not only
# within the same module, but also across modules as long as
# it is in the same Python interpreter process.

FORMATTER = logging.Formatter(
    "%(asctime)s — %(name)s — %(levelname)s —"
    "%(funcName)s:%(lineno)d — %(message)s")
<<<<<<< HEAD
=======
LOG_FILE = config.LOG_DIR / 'ml_models.log'
>>>>>>> 6162c318b58b225e0061fccd6c64cd67fe205c1b


def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler
<<<<<<< HEAD
=======


def get_file_handler():
    file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight')
    file_handler.setFormatter(FORMATTER)
    file_handler.setLevel(logging.INFO)
    return file_handler


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)

    logger.setLevel(logging.DEBUG)

    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())

    logger.propagate = False

    return logger
>>>>>>> 6162c318b58b225e0061fccd6c64cd67fe205c1b
