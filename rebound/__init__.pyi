from ctypes import CDLL

from .interruptible_pool import InterruptiblePool as InterruptiblePool
from .particle import Particle as Particle
from .plotting import OrbitPlot as OrbitPlot
from .simulation import Orbit as Orbit, Simulation as Simulation, Variation as Variation, \
    reb_simulation_integrator_mercurius as reb_simulation_integrator_mercurius, \
    reb_simulation_integrator_saba as reb_simulation_integrator_saba, \
    reb_simulation_integrator_sei as reb_simulation_integrator_sei, \
    reb_simulation_integrator_ias15 as reb_simulation_integrator_ias15, \
    reb_simulation_integrator_whfast as reb_simulation_integrator_whfast
from .simulationarchive import SimulationArchive as SimulationArchive

__libpath__: str
clibrebound: CDLL
__version__: str
__build__: str
__githash__: str


class SimulationError(Exception): ...


class Encounter(Exception): ...


class Collision(Exception): ...


class Escape(Exception): ...


class NoParticles(Exception): ...


class ParticleNotFound(Exception): ...
