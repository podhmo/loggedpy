import typing as t
import sys
import os.path
from importlib import import_module
from importlib.machinery import SourceFileLoader
from importlib.util import (
    spec_from_file_location,
    find_spec,
)
from unittest import mock
from functools import partial
import shutil
import logging


class Flavor:
    format = "%(levelname)s\t%(asctime)s\t%(message)s"
    out = sys.stderr
    level = logging.INFO

    def get_logger(self, name):
        return logging.getLogger(name)

    def setup(
        self,
        *,
        level: t.Optional[int] = None,
        out: t.Optional[t.IO] = None,
        format: t.Optional[str] = None
    ):
        logging.basicConfig(
            level=level or self.level,
            format=format or self.format,
            stream=out or self.out,
        )


def patch(logger, name="info"):
    class Wrapper(logging.LoggerAdapter):
        write = getattr(logging.LoggerAdapter, name)

    class SuppressEmptyStringFilter(logging.Filter):
        def filter(self, record):
            return bool(record.msg.strip())

    internal = logger
    while hasattr(internal, "logger"):
        internal = internal.logger
    internal.addFilter(SuppressEmptyStringFilter())
    return mock.patch("builtins.print", partial(print, file=Wrapper(logger, {}), end=""))


def get_flavor(path) -> Flavor:  # using protocol (types)
    if path.startswith(":"):
        return globals()[path[1:]]()
    else:
        module, name = path.rsplit(":", 1)
        if os.path.exists(module):
            module_id = module.replace(".", "_").replace("-", "_")
            m = SourceFileLoader(module_id, module).load_module()
        else:
            m = import_module(module)
        return getattr(m, name)()


def run(
    flavor: Flavor,  # using protocol (types)
    *,
    filepath: t.Optional[str],
    python_module: t.Optional[str],
    args: t.Sequence[str],
) -> None:
    if python_module is not None:
        # for: python -m <module>
        if filepath is not None:
            args.insert(0, filepath)
        spec = find_spec(python_module)
        sys.argv[1:] = args
        flavor.setup(level=logging.DEBUG)  # xxx
        with patch(flavor.get_logger(spec.name)):
            return SourceFileLoader("__main__", spec.origin).load_module()
    elif os.path.exists(filepath) and not os.path.isdir(filepath):
        # for: python <file>
        spec = spec_from_file_location("__main__", filepath)
        sys.argv[1:] = args
        flavor.setup(level=logging.DEBUG)  # xxx
        with patch(flavor.get_logger(spec.name)):
            return SourceFileLoader("__main__", spec.origin).load_module()
    else:
        # for: <command>
        cmdpath = shutil.which(filepath)
        if not cmdpath:
            raise RuntimeError(f"not supported: {sys.argv}")

        sys.argv = [filepath, *args]
        flavor.setup(level=logging.DEBUG)  # xxx
        with patch(flavor.get_logger(os.path.basename(cmdpath))):
            return SourceFileLoader("__main__", cmdpath).load_module()
