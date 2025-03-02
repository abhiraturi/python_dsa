import logging

# DIfferent configs for logging

# normal config
# logging.basicConfig(level=logging.WARNING)

# writing to a file
# logging.basicConfig(level=logging.WARNING,filename="/Users/abhishekraturi/Desktop/Git/python_dsa/implement_logging/logger_2/app.log",filemode='w')

# writing to a file with formatted messages
logging.basicConfig(level=logging.INFO,filename="/Users/abhishekraturi/Desktop/Git/python_dsa/implement_logging/logger_2/app.log",filemode='w',format="%(asctime)s %(levelname)s %(message)s")


# logging.debug("debug messages")
# logging.info("info messages")
# logging.warning("warning messages")
# logging.error("error messages")
# logging.critical("critical messages")

x=2

logging.info(f"value of x is {x}")

try:
    a=1/0
except Exception as e:
    logging.exception(f"testing exception value for x is {x}")