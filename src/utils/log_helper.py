import logging
import inspect
import datetime

class Log:
    # logging.basicConfig(format=)
    _initialized = False
    _level = logging.INFO
    _formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | [%(funcName)s() - %(lineno)d]: %(message)s')
    logging.Formatter.default_msec_format = '%s.%03d'

    @staticmethod
    def initialize(level=logging.INFO):
        if not Log._initialized:
            Log._level = level
            Log._initialized = True

    @staticmethod
    def _get_logger(name):
        logger = logging.getLogger(name)
        logger.setLevel(Log._level)

        if not logger.handlers:  # Avoid adding multiple handlers to the same logger
            # create file handler
            filename = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            file_handler = logging.FileHandler(f'{filename}.log', mode='w')
            file_handler.setFormatter(Log._formatter)
            logger.addHandler(file_handler)

            # create console handler
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(Log._formatter)
            logger.addHandler(console_handler)
        return logger

    @staticmethod
    def _get_previous_method_name():
        stack = inspect.stack()
        if len(stack) > 2:
            return stack[2].function
        return 'N/A'

    @staticmethod
    def i(name, message):
        logger = Log._get_logger(name)
        logger.info(message, stacklevel=2)

    @staticmethod
    def d(name, message):
        logger = Log._get_logger(name)
        logger.debug(message, stacklevel=2)

    @staticmethod
    def e(name, message):
        logger = Log._get_logger(name)
        logger.error(message, stacklevel=2)

    @staticmethod
    def w(name, message):
        logger = Log._get_logger(name)
        logger.warning(message, stacklevel=2)

    @staticmethod
    def c(name, message):
        logger = Log._get_logger(name)
        logger.critical(message, stacklevel=2)