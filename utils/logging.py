import sys
import logging

from loguru import logger

from utils import settings


class InterceptHandler(logging.Handler):
    LEVELS_MAP = {
        logging.CRITICAL: "CRITICAL",
        logging.ERROR: "ERROR",
        logging.WARNING: "WARNING",
        logging.INFO: "INFO",
        logging.DEBUG: "DEBUG",
    }

    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


def clear_handlers() -> None:
    for name in logging.root.manager.loggerDict.keys():
        logging.getLogger(name).handlers = []
        logging.getLogger(name).propagate = True


def setup() -> None:
    # logger.add(sys.stderr, format="{level} {time} {message}", filter="my_module", level="INFO")
    # logger.add(config.LOGS_BASE_PATH + "/file_{time}.log")
    clear_handlers()

    logging.root.setLevel(logging.INFO)
    if settings.debug:
        logging.root.setLevel(logging.DEBUG)

    logging.getLogger().handlers = [InterceptHandler()]

    logger.configure(handlers=[{"sink": sys.stdout}])
