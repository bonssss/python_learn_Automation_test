import logging
from logging import Logger

logger= logging.getLogger(__name__)

filehandler= logging.FileHandler("logfile.log")
logger.addHandler(filehandler)

logger.critical("critical issue")
logger.debug("debug")

def test_logging_info():
    print("this info logging")
