import re

from collections.abc import Mapping
from yaml import load, FullLoader


class Content(Mapping):
    __delimiter = r"^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)

    @classmethod
    def load(cls, string):
       _, fm, content = cls.__regex.split(string, 2)
       metadata = load(fm, Loader=FullLoader)
       return cls(metadata, content)

    def __init__(self, metadata, content):
        self.data = metadata
        content = {"content": self.data}