from ctypes import Structure, c_int
from typing import Any, Optional, Callable, Sequence, Iterator, Literal, Iterable, Tuple, Union

import numpy as np

from . import Simulation
from .types import IntBoolean


class SimulationArchive(Structure):
    setup: Callable
    setup_args: Sequence
    process_warnings: bool
    warnings: c_int
    tmin: float
    tmax: float

    def __init__(self, filename: str, setup: Optional[Callable] = ..., setup_args: Sequence = ...,
                 process_warnings: bool = ..., reuse_index: Optional[SimulationArchive] = ...) -> None: ...

    def __del__(self) -> None: ...

    def __getitem__(self, key: int) -> Simulation: ...

    def __setitem__(self, key: int, value: Any) -> None: ...

    def __delitem__(self, key: int) -> None: ...

    def __iter__(self) -> Iterator[Simulation]: ...

    def __len__(self) -> int: ...

    def getSimulation(self, t: float, mode: Literal["snapshot", "close", "exact"] = ...,
                      keep_unsynchronized: IntBoolean = ...) -> Simulation: ...

    def getSimulations(self, times: Iterable[float], **kwargs: Any) -> Iterator[Simulation]: ...

    def getBezierPaths(self, origin: Union[None, int, Literal["com"]] = ...) -> Tuple[np.ndarray, np.ndarray]: ...
