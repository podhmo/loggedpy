import logging
import loggedpy


class Driver(loggedpy.Driver):
    format = "%(levelname)s\t%(asctime)s\t%(name)s\tin\t%(filename)s:%(lineno)s\t%(funcName)s\t%(message)s"
    level = logging.DEBUG
