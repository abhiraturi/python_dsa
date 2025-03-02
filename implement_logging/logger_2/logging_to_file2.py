import logging

# writing to a file with formatted messages
logging.basicConfig(level=logging.INFO,filename="/Users/abhishekraturi/Desktop/Git/python_dsa/implement_logging/logger_2/app.log",filemode='w',format="%(asctime)s %(levelname)s %(message)s")


# create custom logger
logger=logging.getLogger(__name__)

# define handler to send the logs to a different file
handler =logging.FileHandler("/Users/abhishekraturi/Desktop/Git/python_dsa/implement_logging/logger_2/app2.log")

# create a formatter
formatter=logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")

# Now, set the formatter for the handler
handler.setFormatter(formatter)

# add handler to the logger
logger.addHandler(handler)

logger.info(f"Testing custom logger")