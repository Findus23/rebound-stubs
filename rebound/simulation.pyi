from collections import MutableMapping
from ctypes import Structure, _Pointer, c_void_p, c_uint, c_uint32, c_ulong, Array, c_double
from typing import Any, Optional, Dict, List, Tuple, Callable, Union, Literal, Iterator, overload

from . import Particle
from .types import HashType, EnumDict, IntBoolean

INTEGRATORS: EnumDict
BOUNDARIES: EnumDict
GRAVITIES: EnumDict
COLLISIONS: EnumDict
VISUALIZATIONS: EnumDict
WHFAST_KERNELS: EnumDict
WHFAST_COORDINATES: EnumDict
SABA_TYPES: EnumDict
EOS_TYPES: EnumDict
BINARY_WARNINGS: List[Tuple[bool, int, str]]


class reb_hash__Pointer_pair(Structure):
    hash: int
    index: int


class reb_vec3d(Structure):
    x: float
    y: float
    z: float


class reb_dp7(Structure):
    p0: _Pointer[float]
    p1: _Pointer[float]
    p2: _Pointer[float]
    p3: _Pointer[float]
    p4: _Pointer[float]
    p5: _Pointer[float]
    p6: _Pointer[float]


class reb_ghostbox(Structure):
    shiftx: float
    shifty: float
    shiftz: float
    shiftvx: float
    shiftvy: float
    shiftvz: float


class reb_collision(Structure):
    p1: int
    p2: int
    gb: reb_ghostbox
    time: float
    ri: int

    def __repr__(self) -> str: ...


class reb_simulation_integrator_sei(Structure):
    OMEGA: float
    OMEGAZ: float
    _lastdt: float
    _sindt: float
    _tandt: float
    _sindtz: float
    _tandtz: float


class reb_simulation_integrator_ias15(Structure):
    epsilon: float
    min_dt: float
    epsilon_global: int
    neworder: int
    _iterations_max_exceeded: int
    _allocatedN: int
    _at: _Pointer[float]
    _x0: _Pointer[float]
    _v0: _Pointer[float]
    _a0: _Pointer[float]
    _csx: _Pointer[float]
    _csv: _Pointer[float]
    _csa0: _Pointer[float]
    _g: reb_dp7
    _b: reb_dp7
    _csb: reb_dp7
    _e: reb_dp7
    _br: reb_dp7
    _er: reb_dp7
    _map: _Pointer[int]
    _map_allocated_n: _Pointer[int]

    def __repr__(self) -> str: ...


class reb_simulation_integrator_saba(Structure):
    _type: int
    safe_mode: IntBoolean
    is_synchronized: IntBoolean
    keep_unsynchronized: IntBoolean

    @property
    def type(self) -> str: ...

    @type.setter
    def type(self, value: str) -> None: ...


class reb_simulation_integrator_whfast(Structure):
    corrector: int
    corrector2: int
    _kernel: int
    _coordinates: int
    recalculate_coordinates_this_timestep: IntBoolean
    safe_mode: IntBoolean
    _p_jh: _Pointer[Particle]
    _p_temp: _Pointer[Particle]
    keep_unsynchronized: IntBoolean
    is_synchronized: IntBoolean
    _allocatedN: int
    _timestep_warning: int
    _recalculate_coordinates_but_not_synchronized_warning: int

    def __repr__(self) -> str: ...

    @property
    def coordinates(self) -> str: ...

    @coordinates.setter
    def coordinates(self, value: str) -> None: ...

    @property
    def kernel(self) -> str: ...

    @kernel.setter
    def kernel(self, value: str) -> None: ...


class Orbit(Structure):
    d: float
    v: float
    h: float
    P: float
    n: float
    a: float
    e: float
    inc: float
    Omega: float
    omega: float
    pomega: float
    f: float
    M: float
    l: float
    theta: float
    T: float
    rhill: float


class Simulation(Structure):
    t: float
    G: float
    softening: float
    dt: float
    dt_last_done: float
    steps_done: int
    N: int
    N_var: int
    var_config_N: int
    var_config: _Pointer[Variation]
    N_active: int
    testparticle_type: int
    _particle_lookup_table: _Pointer[reb_hash__Pointer_pair]
    hash_ctr: int
    N_lookup: int
    allocatedN_lookup: int
    allocated_N: int
    _particles: _Pointer[Particle]
    gravity_cs: _Pointer[reb_vec3d]
    gravity_cs_allocatedN: int
    _tree_root: c_void_p
    _tree_needs_update: int
    opening_angle2: float
    _status: int
    exact_finish_time: int
    force_is_velocity_dependent: c_uint
    gravity_ignore: c_uint
    _output_timing_last: float
    _display_clock: int
    save_messages: int
    messages: c_void_p
    exit_max_distance: float
    exit_min_distance: float
    usleep: float
    display_data: _Pointer[reb_display_data]
    track_energy_offset: int
    energy_offset: float
    walltime: float
    python_unit_t: int
    python_unit_l: int
    python_unit_m: int
    boxsize: reb_vec3d
    boxsize_max: float
    root_size: float
    root_n: int
    root_nx: int
    root_ny: int
    root_nz: int
    nghostx: int
    nghosty: int
    nghostz: int
    collision_resolve_keep_sorted: int
    collisions: c_void_p
    collisions_allocatedN: int
    minimum_collision_velocity: float
    collisions_plog: float
    max_radius: Array[c_double]
    collisions_Nlog: int
    _calculate_megno: int
    _megno_Ys: float
    _megno_Yss: float
    _megno_cov_Yt: float
    _megno_var_t: float
    _megno_mean_t: float
    _megno_mean_Y: float
    _megno_n: int
    _rand_seed: int
    simulationarchive_version: int
    simulationarchive_size_first: int
    simulationarchive_size_snapshot: int
    simulationarchive_auto_interval: float
    simulationarchive_auto_walltime: float
    simulationarchive_auto_step: int
    simulationarchive_next: float
    simulationarchive_next_step: int
    _simulationarchive_filename: bytes
    _visualization: int
    _collision: int
    _integrator: int
    _boundary: int
    _gravity: int
    ri_sei: reb_simulation_integrator_sei
    ri_whfast: reb_simulation_integrator_whfast
    ri_saba: reb_simulation_integrator_saba
    ri_ias15: reb_simulation_integrator_ias15
    ri_mercurius: reb_simulation_integrator_mercurius
    ri_janus: reb_simulation_integrator_janus
    ri_eos: reb_simulation_integrator_eos
    # _additional_forces: CFUNCTYPE(None, _Pointer[Simulation])
    # _pre_timestep_modifications: CFUNCTYPE(None, _Pointer[Simulation])
    # _post_timestep_modifications: CFUNCTYPE(None, _Pointer[Simulation])
    # _heartbeat: CFUNCTYPE(None, _Pointer[Simulation])
    # _display_heartbeat: CFUNCTYPE(None, _Pointer[Simulation])
    # _coefficient_of_restitution: CFUNCTYPE(float, _Pointer[Simulation], float)
    # _collision_resolve: CFUNCTYPE(int, _Pointer[Simulation], reb_collision)
    # _free_particle_ap: CFUNCTYPE(None, _Pointer[Particle])
    # _extras_cleanup: CFUNCTYPE(None, _Pointer[Simulation])
    extras: c_void_p

    def __new__(cls, *args: Any, **kw: Any): ...

    def __init__(self) -> None: ...

    def __repr__(self) -> str: ...

    # Deprecated methods
    # @classmethod
    # def from_archive(cls, filename: Any, snapshot: int = ...): ...
    #
    # @classmethod
    # def from_file(cls, filename: Any): ...

    def copy(self) -> Simulation: ...

    def cite(self) -> None: ...

    visualization: int = ...

    def getWidget(self, **kwargs: Any): ...

    def refreshWidgets(self) -> None: ...

    # not sure if those should be set manually
    # simulationarchive_auto_interval: int
    # simulationarchive_auto_walltime: int
    # simulationarchive_auto_step: int

    def automateSimulationArchive(self, filename: str, interval: Optional[float] = ..., walltime: Optional[float] = ...,
                                  step: Optional[int] = ..., deletefile: bool = ...) -> None: ...

    def simulationarchive_snapshot(self, filename: str, deletefile: bool = ...) -> None: ...

    @property
    def simulationarchive_filename(self) -> str: ...

    def process_messages(self) -> None: ...

    def __del__(self) -> None: ...

    def __eq__(self, other: object) -> bool: ...

    def __add__(self, other: Simulation) -> Simulation: ...

    def __iadd__(self, other: Simulation) -> Simulation: ...

    def __sub__(self, other: Simulation) -> Simulation: ...

    def __isub__(self, other: Simulation) -> Simulation: ...

    def __mul__(self, other: float) -> Simulation: ...

    def __imul__(self, other: float) -> Simulation: ...

    def __rmul__(self, other: float) -> Simulation: ...

    def __div__(self, other: float) -> Simulation: ...

    def __idiv__(self, other: float) -> Simulation: ...

    def __truediv__(self, other: float) -> Simulation: ...

    def __itruediv__(self, other: float) -> Simulation: ...

    def multiply(self, scalar_pos: float, scalar_vel: float) -> None: ...

    def status(self) -> None: ...

    @property
    def additional_forces(self) -> None: ...

    @additional_forces.setter
    def additional_forces(self, func: Callable[[_Pointer[Simulation]], None]) -> None: ...

    @property
    def pre_timestep_modifications(self) -> None: ...

    @pre_timestep_modifications.setter
    def pre_timestep_modifications(self, func: Callable[[_Pointer[Simulation]], None]) -> None: ...

    @property
    def post_timestep_modifications(self) -> None: ...

    @post_timestep_modifications.setter
    def post_timestep_modifications(self, func: Callable[[_Pointer[Simulation]], None]) -> None: ...

    @property
    def heartbeat(self) -> None: ...

    @heartbeat.setter
    def heartbeat(self, func: Callable[[_Pointer[Simulation]], None]) -> None: ...

    @property
    def coefficient_of_restitution(self) -> None: ...

    @coefficient_of_restitution.setter
    def coefficient_of_restitution(self, func: Callable[[_Pointer[Simulation], float], float]) -> None: ...

    @property
    def collision_resolve(self) -> None: ...

    @collision_resolve.setter
    def collision_resolve(self, func: Union[
        Literal["merge:", "hardsphere"],
        Callable[[_Pointer[Simulation], reb_collision], float]
    ]) -> None: ...

    @property
    def free_particle_ap(self) -> None: ...

    @free_particle_ap.setter
    def free_particle_ap(self, func: Callable[[_Pointer[Particles]], None]) -> None: ...

    @property
    def N_real(self) -> int: ...

    @property
    def integrator(self) -> str: ...

    @integrator.setter
    def integrator(self, value: Union[int, str]) -> None: ...

    @property
    def boundary(self) -> str: ...

    @boundary.setter
    def boundary(self, value: Union[int, str]) -> None: ...

    @property
    def gravity(self) -> str: ...

    @gravity.setter
    def gravity(self, value: Union[int, str]) -> None: ...

    @property
    def collision(self) -> str: ...

    @collision.setter
    def collision(self, value: Union[int, str]) -> None: ...

    @property
    def units(self) -> Dict[str, str]: ...

    @units.setter
    def units(self, newunits: Tuple[str, str, str]) -> None: ...

    # python_unit_l: Any = ...
    # python_unit_t: Any = ...
    # python_unit_m: Any = ...

    def update_units(self, newunits: Tuple[str, str, str]) -> None: ...

    def convert_particle_units(self, *args: Any) -> None: ...

    def add_variation(self, order: int = ..., first_order: Optional[Variation] = ...,
                      first_order_2: Optional[Variation] = ..., testparticle: int = ...): ...

    def init_megno(self, seed: Optional[int] = ...) -> None: ...

    def calculate_megno(self) -> float: ...

    def calculate_lyapunov(self) -> float: ...

    #TODO: support other arguments
    def add(self, particle: Optional[Particle] = ..., **kwargs: Any) -> None: ...

    @property
    def particles(self) -> Particles: ...

    @particles.deleter
    def particles(self) -> None: ...

    def remove(self, index: Optional[int] = ..., hash: Optional[HashType] = ..., keepSorted: bool = ...) -> None: ...

    def particles_ascii(self, prec: int = ...) -> str: ...

    def add_particles_ascii(self, s: str) -> None: ...

    def calculate_orbits(self, primary: Optional[Particle] = ..., jacobi_masses: bool = ...,
                         # deprecated options:
                         # heliocentric: Optional[bool] = ..., barycentric: Optional[bool] = ...
                         ) -> Orbit: ...

    def calculate_com(self, first: int = ..., last: Optional[int] = ...) -> Particle: ...

    def serialize_particle_data(self, **kwargs: Any) -> None: ...

    def set_serialized_particle_data(self, **kwargs: Any) -> None: ...

    def move_to_hel(self) -> None: ...

    def move_to_com(self) -> None: ...

    def calculate_energy(self) -> float: ...

    def calculate_angular_momentum(self) -> Tuple[float, float, float]: ...

    def configure_box(self, boxsize: float, root_nx: int = ..., root_ny: int = ..., root_nz: int = ...) -> None: ...

    def configure_ghostboxes(self, nghostx: int = ..., nghosty: int = ..., nghostz: int = ...) -> None: ...

    def save(self, filename: str) -> None: ...

    def step(self) -> None: ...

    def steps(self, N_steps: int) -> None: ...

    # exact_finish_time: int = ...

    def integrate(self, tmax: float, exact_finish_time: IntBoolean = ...) -> None: ...

    def integrator_reset(self) -> None: ...

    def integrator_synchronize(self) -> None: ...

    def tree_update(self) -> None: ...


class Variation(Structure):
    _sim: _Pointer[Simulation]
    order: int
    index: int
    testparticle: int
    index_1st_order_a: int
    index_1st_order_b: int

    def vary(self, particle_index: int, variation: str, variation2: Optional[str] = ...,
             primary: Optional[Particle] = ...) -> None: ...

    @property
    def particles(self) -> List[Particle]: ...  #TODO: check if correct


class reb_particle_int(Structure):
    x: int
    y: int
    z: int
    vx: int
    vy: int
    vz: int


class reb_simulation_integrator_janus(Structure):
    scale_pos: float
    scale_vel: float
    order: int
    recalculate_integer_coordinates_this_timestep: IntBoolean
    p_int: _Pointer[reb_particle_int]
    _allocated_N: int


class reb_simulation_integrator_eos(Structure):
    _phi0: int
    _phi1: int
    n: int
    safe_mode: IntBoolean
    is_synchronized: IntBoolean

    def __repr__(self) -> str: ...

    @property
    def phi0(self) -> str: ...

    @phi0.setter
    def phi0(self, value: str) -> None: ...

    @property
    def phi1(self) -> str: ...

    @phi1.setter
    def phi1(self, value: str) -> None: ...


class reb_simulation_integrator_mercurius(Structure):
    L: Callable[[_Pointer[Simulation], float, float], float]
    hillfac: float
    recalculate_coordinates_this_timestep: IntBoolean
    recalculate_dcrit_this_timestep: IntBoolean
    safe_mode: IntBoolean
    is_synchronized: IntBoolean
    mode: int
    _encounterN: int
    _encounterNactive: int
    _tponly_encounter: int
    _allocatedN: int
    _allocatedN_additionalforces: int
    _dcrit_allocatedN: int
    _dcrit: _Pointer[float]
    _particles_backup: _Pointer[Particle]
    _particles_backup_additionalforces: _Pointer[Particle]
    _encounter_map: _Pointer[int]
    _com_pos: reb_vec3d
    _com_vel: reb_vec3d

    def __repr__(self) -> str: ...


class timeval(Structure):
    tv_sec: int
    tv_usec: int


#TODO: check if ctypes should be used above

class reb_display_data(Structure):
    r: _Pointer[Simulation]
    r_copy: _Pointer[Simulation]
    particle_data: c_void_p
    orbit_data: c_void_p
    particles_copy: _Pointer[Particle]
    p_jh_copy: _Pointer[Particle]
    allocated_N: int
    allocated_N_whfast: int
    opengl_enabled: int
    scale: float
    mouse_x: float
    mouse_y: float
    retina: float


ParticleKey = Union[c_uint32, c_uint, c_ulong, str, int]


class Particles(MutableMapping):
    sim: Simulation

    def __init__(self, sim: Simulation) -> None: ...

    @overload
    def __getitem__(self, key: ParticleKey) -> Particle: ...

    @overload
    def __getitem__(self, key: slice) -> List[Particle]: ...

    def __setitem__(self, key: ParticleKey, value: Particle) -> None: ...

    def __delitem__(self, key: ParticleKey) -> None: ...

    def __iter__(self) -> Iterator[Particle]: ...

    def __len__(self) -> int: ...
