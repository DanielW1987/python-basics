import logging

# the default log level is 'warn' and the default log output is the console
logging.basicConfig(filename="mylog.log", level=logging.DEBUG)
logging.critical("critical")
logging.error("error")
logging.warning("warn")
logging.info("info")
logging.debug("debug")
