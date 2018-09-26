import logging
import loggedpy


class Flavor(loggedpy.Flavor):
    format = "%(levelname)s\t%(asctime)s\t%(name)s\tin\t%(filename)s:%(lineno)s\t%(funcName)s\t%(message)s"
    level = logging.DEBUG
