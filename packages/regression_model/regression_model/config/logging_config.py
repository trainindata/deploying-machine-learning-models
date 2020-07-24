import logging
import sys


# Multiple calls to logging.getLogger('someLogger') return a
# reference to the same logger object.  This is true not only
# within the same module, but also across modules as long as
# it is in the same Python interpreter process.

# The structure of the FORMATTER is:
# 1. A datetime stamp
# 2. The name of the logger
# 3. The level name: DEBUG, INFO...
# 4. The function name: the function from which the log was generated
# 5. The line number within that function
# 6. The actual message that we log
FORMATTER = logging.Formatter(
    "%(asctime)s — %(name)s — %(levelname)s —" "%(funcName)s:%(lineno)d — %(message)s"
)


def get_console_handler():
    # The console handler will get what is diplayed in either the command prompt or the terminal
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler
