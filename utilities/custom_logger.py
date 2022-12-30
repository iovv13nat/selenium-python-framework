import inspect
import logging

def customLogger(logLevel=logging.DEBUG):
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG)#By default, logs all messages

    fileHandler = logging.FileHandler("automation.log", mode='w')
    fileHandler.setLevel(logLevel)



    formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s:', datefmt ='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formater)
    logger.addHandler(fileHandler)

    return logger
