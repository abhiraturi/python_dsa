'''

-------------- METHOD 1 - Simple Way ----------------------------
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="/Users/abhishekraturi/Desktop/Git/python_dsa/implement_logging/logger_2/colored_log.log"
)

'''


'''
-------------- METHOD 2 - Colored Logging Way (colored can only be on console not on file) ----------------------------
'''

import logging

# Define ANSI color codes
RESET = "\033[0m"
COLORS = {
    "DEBUG": "\033[94m",   # Blue
    "INFO": "\033[92m",    # Green
    "WARNING": "\033[93m", # Yellow
    "ERROR": "\033[91m",   # Red
    "CRITICAL": "\033[41m",# Red Background
}

# Custom log formatter with colors
class ColoredFormatter(logging.Formatter):
    def format(self, record):
        log_color = COLORS.get(record.levelname, RESET)  # Get color for the level
        log_message = super().format(record)  # Use default formatting
        return f"{log_color}{log_message}{RESET}"  # Add color & reset

# Set up logging
formatter = ColoredFormatter(
    "%(asctime)s %(levelname)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)

handler = logging.StreamHandler()  # Output logs to console
handler.setFormatter(formatter)


logging.basicConfig(
    level=logging.DEBUG,
    handlers=[handler]
)

