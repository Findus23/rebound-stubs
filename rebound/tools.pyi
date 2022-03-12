from ctypes import c_uint32, c_uint, c_ulong
from typing import Union

from .types import HashType


def hash(key: HashType) -> Union[c_uint32, c_uint, c_ulong]: ...


def mod2pi(x: float) -> float: ...


def M_to_f(e: float, M: float) -> float: ...


def E_to_f(e: float, E: float) -> float: ...


def M_to_E(e: float, M: float) -> float: ...
