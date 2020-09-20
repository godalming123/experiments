from logging import *
LoggerFormat = "%(Levelname)s %(asctime)s - %(message)s"
basicConfig (filename = "logger.log", level=DEBUG, format = LoggerFormat)
logger = getLogger ()

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
