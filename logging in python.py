import logging

LoggerFormat = "%(Levelname)s %(asctime)s - %(message)s"
logging.basicConfig (filename = "logger.log", level="DEBUG")

logger = logging.getLogger ()

logger.debug ("why did I tell the logger to warn me about telling the logger to warn me")
logger.info ("my logger file")
logger.warning ("why did you put warning here, also why did you put an error on line 11 and a critical on line 12")
logger.error ("error")
logger.critical ("critical")

try :
  #code
  pass

except error as e:
  logger.error (e)
