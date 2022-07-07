import os
import sys
import sys

sys.path.append('/tf/packages/regression_model/')
print(sys.path)
from regression_model.config import config

with open(os.path.join(config.PACKAGE_ROOT, 'VERSION')) as version_file:

    __version__ = version_file.read().strip()