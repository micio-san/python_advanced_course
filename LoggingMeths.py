import logging
#only messages by level warining are printed by default
logging.basicConfig(level=logging.DEBUG, datefmt='%d/%m/%Y %H:%M:%S', format='%(asctime)s %(message)s')
logging.debug("this is a debugging error")
logging.info("information about the program")
logging.warning("something to check out")
logging.error("an unexpected problem occurred")
logging.critical("crash app")

logger = logging.getLogger(__name__)
logger.info('custom_logger')
logger.propagate(False)
stream_handler=logging.StreamHandler()
file_h=logging.FileHandler("file.log")
#for each logger handler and format
stream_handler.setLevel(logging.warning)
file_h.setLevel(logging.ERROR)
