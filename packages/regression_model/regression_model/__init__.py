import logging
<<<<<<< HEAD
=======
import os
>>>>>>> 0ed582465d48f8120b8ddf1b901da14d3e5c5865

from regression_model.config import config
from regression_model.config import logging_config


<<<<<<< HEAD
VERSION_PATH = config.PACKAGE_ROOT / 'VERSION'

=======
>>>>>>> 0ed582465d48f8120b8ddf1b901da14d3e5c5865
# Configure logger for use in package
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging_config.get_console_handler())
logger.propagate = False


<<<<<<< HEAD
with open(VERSION_PATH, 'r') as version_file:
=======
with open(os.path.join(config.PACKAGE_ROOT, 'VERSION')) as version_file:
>>>>>>> 0ed582465d48f8120b8ddf1b901da14d3e5c5865
    __version__ = version_file.read().strip()
