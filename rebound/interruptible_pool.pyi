from multiprocessing.pool import Pool
from typing import Any, Optional, Callable, Iterable


class InterruptiblePool(Pool):
    wait_timeout: int = ...

    def __init__(self, processes: Optional[int] = ..., initializer: Optional[Callable[..., None]] = ...,
                 initargs: Iterable[Any] = ..., **kwargs: Any) -> None: ...

    def map(self, func: Callable, iterable: Iterable, chunksize: Optional[int] = ...): ...
