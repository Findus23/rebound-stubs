from ctypes import Structure, c_uint32
from typing import Any, Optional, List

from . import Simulation, Orbit
from .types import HashType


class Particle(Structure):
    m: float
    x: float
    y: float
    z: float
    vx: float
    vy: float
    vz: float
    ax: float
    ay: float
    az: float
    r: float
    lastcollision: float
    c: Any  # TODO: find out documentation
    ap: Any  # TODO: find out documentation

    def __repr__(self) -> str: ...

    def __init__(self, simulation: Optional[Simulation] = ..., particle: Optional[Particle] = ...,
                 m: Optional[float] = ..., x: Optional[float] = ..., y: Optional[float] = ..., z: Optional[float] = ...,
                 vx: Optional[float] = ..., vy: Optional[float] = ..., vz: Optional[float] = ...,
                 primary: Optional[Particle] = ..., a: Optional[float] = ..., P: Optional[float] = ...,
                 e: Optional[float] = ..., inc: Optional[float] = ..., Omega: Optional[float] = ...,
                 omega: Optional[float] = ..., pomega: Optional[float] = ..., f: Optional[float] = ...,
                 M: Optional[float] = ..., l: Optional[float] = ..., theta: Optional[float] = ...,
                 T: Optional[float] = ..., r: Optional[float] = ..., date: Optional[str] = ...,
                 variation: Optional[str] = ..., variation2: Optional[str] = ..., h: Optional[HashType] = ...,
                 k: Optional[float] = ..., ix: Optional[float] = ..., iy: Optional[float] = ..., hash: HashType = ...,
                 jacobi_masses: bool = ...): ...

    def copy(self) -> Particle: ...

    def calculate_orbit(self, primary: Optional[Particle], G: Optional[float]) -> Orbit: ...

    def sample_orbit(self, Npts: int, primary: Optional[Particle], trailing: bool,
                     timespan: Optional[float], useTrueAnomaly: Optional[bool],
                     duplicateEndpoint: Optional[bool]): ... #TODO: return value

    def __pow__(self, other: Particle) -> Particle: ...

    def __add__(self, other: Particle) -> Particle: ...

    def __iadd__(self, other: Particle) -> Particle: ...

    def __sub__(self, other: Particle) -> Particle: ...

    def __isub__(self, other: Particle) -> Particle: ...

    def __mul__(self, other: float) -> Particle: ...

    def __imul__(self, other: float) -> Particle: ...

    def __rmul__(self, other: float) -> Particle: ...

    def __div__(self, other: float) -> Particle: ...

    def __idiv__(self, other: float) -> Particle: ...

    def __truediv__(self, other: float) -> Particle: ...

    def __itruediv__(self, other: float) -> Particle: ...

    @property
    def index(self) -> int: ...

    @property
    def xyz(self) -> List[float]: ...

    @xyz.setter
    def xyz(self, value: List[float]) -> None: ...

    @property
    def vxyz(self) -> List[float]: ...

    @vxyz.setter
    def vxyz(self, value: List[float]) -> None: ...

    @property
    def d(self) -> float: ...

    @property
    def v(self) -> float: ...

    @property
    def h(self) -> float: ...

    @property
    def P(self) -> float: ...

    @P.setter
    def P(self, value: float) -> None: ...

    @property
    def n(self) -> float: ...

    @property
    def a(self) -> float: ...

    @a.setter
    def a(self, value: float) -> None: ...

    @property
    def rhill(self) -> float: ...

    @property
    def e(self) -> float: ...

    @e.setter
    def e(self, value: float) -> None: ...

    @property
    def inc(self) -> float: ...

    @inc.setter
    def inc(self, value: float) -> None: ...

    @property
    def Omega(self) -> float: ...

    @Omega.setter
    def Omega(self, value: float) -> None: ...

    @property
    def omega(self) -> float: ...

    @omega.setter
    def omega(self, value: float) -> None: ...

    @property
    def pomega(self) -> float: ...

    @pomega.setter
    def pomega(self, value: float) -> None: ...

    @property
    def f(self) -> float: ...

    @f.setter
    def f(self, value: float) -> None: ...

    @property
    def M(self) -> float: ...

    @property
    def l(self) -> float: ...

    @l.setter
    def l(self, value: float) -> None: ...

    @property
    def theta(self) -> float: ...

    @theta.setter
    def theta(self, value: float) -> None: ...

    @property
    def T(self) -> float: ...

    @T.setter
    def T(self, value: float) -> None: ...

    @property
    def orbit(self) -> Orbit: ...

    @property
    def jacobi_com(self): ...  #TODO: correct typing

    @property
    def hash(self) -> c_uint32: ...

    @hash.setter
    def hash(self, value: HashType) -> None: ...

    def _cpcoords(self, p: Particle) -> None: ...
