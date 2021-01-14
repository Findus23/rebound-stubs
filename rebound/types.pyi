from ctypes import c_uint32, c_ulong, c_uint
from typing import Union

HashType = Union[c_uint32, c_uint, c_ulong, str, int]
