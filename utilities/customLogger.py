import logging
import inspect
import sys


class LogGen:
    @staticmethod
    def loggen(logLevel=logging.DEBUG):
        # set class/method name from where it is calling
        logger_name = inspect.stack()[1][3]
        # create logger
        logger = logging.getLogger(logger_name)
        logger.setLevel(logLevel)
        console = logging.StreamHandler(sys.stdout)  # for console printing
        # file location and set the log level W or a
        fh = logging.FileHandler(".\\Logs\\automation.log", mode='w')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        console.setFormatter(formatter)  # for console printing
        logging.getLogger(logger_name).addHandler(console)  # for console printing
        # add formatter to console or file handler
        fh.setFormatter(formatter)
        # add console handle to logger
        logger.addHandler(fh)
        return logger
