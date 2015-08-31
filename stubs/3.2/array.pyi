# Stubs for array

# Based on http://docs.python.org/3.2/library/array.html

from typing import Any, Iterable, Tuple, List, Iterator, BinaryIO, overload

typecodes = ''

class array:
    def __init__(self, typecode: str,
                 initializer: Iterable[Any] = None) -> None:
        typecode = ''
        itemsize = 0

    def append(self, x: Any) -> None: ...
    def buffer_info(self) -> Tuple[int, int]: ...
    def byteswap(self) -> None: ...
    def count(self, x: Any) -> int: ...
    def extend(self, iterable: Iterable[Any]) -> None: ...
    def frombytes(self, s: bytes) -> None: ...
    def fromfile(self, f: BinaryIO, n: int) -> None: ...
    def fromlist(self, list: List[Any]) -> None: ...
    def fromstring(self, s: bytes) -> None: ...
    def fromunicode(self, s: str) -> None: ...
    def index(self, x: Any) -> int: ...
    def insert(self, i: int, x: Any) -> None: ...
    def pop(self, i: int = -1) -> Any: ...
    def remove(self, x: Any) -> None: ...
    def reverse(self) -> None: ...
    def tobytes(self) -> bytes: ...
    def tofile(self, f: BinaryIO) -> None: ...
    def tolist(self) -> List[Any]: ...
    def tostring(self) -> bytes: ...
    def tounicode(self) -> str: ...

    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[Any]: ...
    def __str__(self) -> str: ...
    def __hash__(self) -> int: ...

    @overload
    def __getitem__(self, i: int) -> Any: ...
    @overload
    def __getitem__(self, s: slice) -> 'array': ...

    def __setitem__(self, i: int, o: Any) -> None: ...
    def __delitem__(self, i: int) -> None: ...
    def __add__(self, x: 'array') -> 'array': ...
    def __mul__(self, n: int) -> 'array': ...
    def __contains__(self, o: object) -> bool: ...