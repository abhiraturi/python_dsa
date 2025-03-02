import logging
import sys
from colorama import Fore, Style, init

# Initialize colorama for Windows support
init(autoreset=True)

class ColoredFormatter(logging.Formatter):
    """Custom formatter to add colors to logs"""
    COLORS = {
        logging.INFO: Fore.GREEN,
        logging.WARNING: Fore.YELLOW,
        logging.ERROR: Fore.RED,
        logging.DEBUG: Fore.CYAN,
        logging.CRITICAL: Fore.MAGENTA,
    }

    def format(self, record):
        log_color = self.COLORS.get(record.levelno, Fore.WHITE)
        log_message = super().format(record)
        return f"{log_color}{log_message}{Style.RESET_ALL}"

def setup_stdout_logger(name="stdout_logger", level=logging.INFO):
    """Set up a custom logger that logs to stdout with colors"""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create a StreamHandler for stdout
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)

    # Define log format with colors
    formatter = ColoredFormatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    # Prevent duplicate handlers
    if logger.hasHandlers():
        logger.handlers.clear()

    logger.addHandler(console_handler)
    return logger

