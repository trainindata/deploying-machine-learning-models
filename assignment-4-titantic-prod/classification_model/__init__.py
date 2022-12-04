import logging

from classification_model.config.core import PACKAGE_ROOT, config


# do not add any handlers other than NullHandler
logging.getLogger(config.app_config.package_name).addHandler(logging.NullHandler())

with open(PACKAGE_ROOT / "VERSION") as version_file:
    __version__ = version_file.read().strip()