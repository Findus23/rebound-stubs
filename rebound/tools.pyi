from ctypes import c_uint32, Union, c_uint, c_ulong

from .types import HashType


def hash(key: HashType) -> Union[c_uint32, c_uint, c_ulong]: ...
