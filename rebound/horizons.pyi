from datetime import datetime
from typing import Optional, Union

from . import Particle


def api_request(particle: str, datestart: Union[str, datetime], dateend: Union[str, datetime], plane: str) -> str:
    ...


def getParticle(particle: Optional[str] = ..., m: Optional[float] = ..., x: Optional[float] = ...,
                y: Optional[float] = ..., z: Optional[float] = ..., vx: Optional[float] = ...,
                vy: Optional[float] = ..., vz: Optional[float] = ..., primary: Optional[float] = ...,
                a: Optional[float] = ..., anom: Optional[float] = ..., e: Optional[float] = ...,
                omega: Optional[float] = ..., inc: Optional[float] = ..., Omega: Optional[float] = ...,
                MEAN: Optional[float] = ..., date: Optional[Union[str, datetime]] = ..., plane: str = ...,
                hash: int = ...) -> Particle: ...
