from ctypes import c_uint32
from typing import Dict, Sequence

from rebound import Particle


def hash_to_unit(hash: c_uint32) -> str: ...


G_SI: float
times_SI: Dict[str, float]
lengths_SI: Dict[str, float]
masses_SI: Dict[str, float]


def units_convert_particle(p: Particle, old_l: str, old_t: str, old_m: str,
                           new_l: str, new_t: str, new_m: str) -> Particle: ...


def convert_mass(mass: float, old_m: str, new_m: str) -> float: ...


def convert_length(length: float, old_l: str, new_l: str) -> float: ...


def convert_vel(vel: float, old_l: str, old_t: str, new_l: str, new_t: str) -> float: ...


def convert_acc(acc: float, old_l: str, old_t: str, new_l: str, new_t: str) -> float: ...


def convert_G(newunits: Sequence[str]) -> float: ...


def check_units(newunits: Sequence[str]) -> Sequence[str]: ...
