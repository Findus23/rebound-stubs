from ctypes import c_uint32, c_ulong, c_uint
from typing import Union, Dict, Literal

HashType = Union[c_uint32, c_uint, c_ulong, str, int]
EnumDict = Dict[str, int]
IntBoolean = Literal[0, 1]
