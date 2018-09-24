import typing as t
from functools import partial
import json
import loggedpy
import monokaki


class Driver(loggedpy.Driver):
    format = "%(levelname)s\t%(asctime)s\t%(name)s\tin\t%(filename)s:%(lineno)s\t%(funcName)s\t%(message)s"

    def get_logger(self, name):
        return monokaki.getLogger(name)

    def setup(
        self,
        *,
        level: t.Optional[int] = None,
        out: t.Optional[t.IO] = None,
        format: t.Optional[str] = None
    ):
        from monokaki.renderer import create_renderer_class
        monokaki.basic_config(
            level=level or self.level,
            format=format or self.format,
            stream=out or self.out,
            renderer=create_renderer_class(
                format or self.format, dumps=partial(json.dumps, indent=2, ensure_ascii=False)
            ),
        )
