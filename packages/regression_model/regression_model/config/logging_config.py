import logging
<<<<<<< HEAD
import sys

=======
from logging.handlers import TimedRotatingFileHandler
import os
import sys

from regression_model.config import config
>>>>>>> 0ed582465d48f8120b8ddf1b901da14d3e5c5865

# Multiple calls to logging.getLogger('someLogger') return a
# reference to the same logger object.  This is true not only
# within the same module, but also across modules as long as
# it is in the same Python interpreter process.

FORMATTER = logging.Formatter(
<<<<<<< HEAD
    "%(asctime)s — %(name)s — %(levelname)s —" "%(funcName)s:%(lineno)d — %(message)s"
)
=======
    "%(asctime)s — %(name)s — %(levelname)s —"
    "%(funcName)s:%(lineno)d — %(message)s")
>>>>>>> 0ed582465d48f8120b8ddf1b901da14d3e5c5865


def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler
