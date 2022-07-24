
import sys
sys.path.append('/tf/packages/ml_api')

from api.config import PACKAGE_ROOT

with open(PACKAGE_ROOT  / 'VERSION') as version_file:

    __version__ = version_file.read().strip()
    #print(__version__)