from typing import Any, Optional, Tuple, Union, List, Iterable

from matplotlib.axes import Axes
from matplotlib.collections import LineCollection
from matplotlib.figure import Figure

from . import Simulation, Particle

Limits = Tuple[float, float]
ColorTuple = Tuple[int, int, int]


def OrbitPlot(sim: Simulation, figsize: Optional[Tuple[float, float]] = ..., fancy: bool = ...,
              slices: Optional[int] = ..., xlim: Optional[Limits] = ..., ylim: Optional[Limits] = ...,
              unitlabel: Optional[str] = ..., color: Union[str, bool, List, None] = ..., periastron: bool = ...,
              orbit_type: str = ..., lw: float = ..., plotparticles: List[int] = ..., primary: Optional[Particle] = ...,
              Narc: int = ...) -> Union[Tuple[Figure, Axes], Tuple[Figure, Axes, Axes, Axes]]: ...


def get_color(color: str) -> ColorTuple: ...


def fading_line(x: Iterable[float], y: Iterable[float], color: Union[str, ColorTuple] = ..., alpha: float = ...,
                fading: bool = ..., fancy: bool = ..., **kwargs: Any) -> LineCollection: ...


def OrbitPlotOneSlice(sim: Simulation, ax: Axes, Narc: int = ..., color: bool = ..., periastron: bool = ...,
                      orbit_type: str = ..., lw: float = ..., axes: str = ..., plotparticles: List[int] = ...,
                      primary: Optional[Particle] = ..., fancy: bool = ..., xlim: Optional[Tuple[float, float]] = ...,
                      ylim: Optional[Tuple[float, float]] = ...) -> None: ...


def OrbitPlotAddFancyStars(ax: Axes, lw: float, slices: float = ...) -> None: ...
