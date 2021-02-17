from ctypes import c_uint32, c_uint, c_ulong
from typing import Union

from .types import HashType


def hash(key: HashType) -> Union[c_uint32, c_uint, c_ulong]: ...
