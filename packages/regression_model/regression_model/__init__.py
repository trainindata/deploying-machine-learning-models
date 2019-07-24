<<<<<<< HEAD
import logging
import os

from regression_model.config import config
from regression_model.config import logging_config


# Configure logger for use in package
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging_config.get_console_handler())
logger.propagate = False
=======
import os

from regression_model.config import config
>>>>>>> 6162c318b58b225e0061fccd6c64cd67fe205c1b


with open(os.path.join(config.PACKAGE_ROOT, 'VERSION')) as version_file:
    __version__ = version_file.read().strip()
