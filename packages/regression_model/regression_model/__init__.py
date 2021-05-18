import logging

from regression_model.config import config
from regression_model.config import logging_config


VERSION_PATH = config.PACKAGE_ROOT / 'VERSION'

# Configure logger for use in package
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging_config.get_console_handler())
logger.propagate = False


with open(VERSION_PATH, 'r') as version_file:
    __version__ = version_file.read().strip()
