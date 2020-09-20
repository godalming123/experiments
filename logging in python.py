import logging

LoggerFormat = "%(Levelname)s %(asctime)s - %(message)s"
logging.basicConfig (filename = "logger.log", level="DEBUG")

logger = logging.getLogger ()

logger.debug ("debug")
logger.info ("info")
logger.warning ("warning")
logger.error ("error")
logger.critical ("critical")

try :
  #code
  pass

except error as e:
  logger.error (e)
