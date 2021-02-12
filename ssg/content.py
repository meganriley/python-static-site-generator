import re

from collections.abc import Mapping
from yaml import load, FullLoader


class Content(Mapping):
    __delimiter = r"^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)

    def load(self, cls, string):
       _, fm, content = __regex.split(string, 2)
       load(fm, Loader=FullLoader)
       return cls(metadata, content)