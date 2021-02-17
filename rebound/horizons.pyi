from typing import Optional

from . import Particle


def getParticle(particle: Optional[str], m: Optional[float], x: Optional[float], y: Optional[float], z: Optional[float],
                vx: Optional[float], vy: Optional[float], vz: Optional[float], primary: Optional[float],
                a: Optional[float], anom: Optional[float], e: Optional[float], omega: Optional[float],
                inc: Optional[float], Omega: Optional[float], MEAN: Optional[float], date: Optional[float],
                plane: str, hash: int) -> Particle: ...
