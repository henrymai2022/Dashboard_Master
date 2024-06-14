import array
from typing import Union
from typing_extensions import final

_InputType = Union[str, bytes, bytearray, memoryview, array.ArrayType[int]]

VERSION: str
XXHASH_VERSION: str
VERSION_TUPLE: tuple[int, ...]

algorithms_available: set[str]

class _Hasher:
    def __init__(self, input: _InputType = ..., seed: int = ...) -> None: ...
    def update(self, input: _InputType) -> None: ...
    def digest(self) -> bytes: ...
    def hexdigest(self) -> str: ...
    def intdigest(self) -> int: ...
    def copy(self) -> _Hasher: ...
    def reset(self) -> None: ...
    @property
    def digestsize(self) -> int: ...
    @property
    def digest_size(self) -> int: ...
    @property
    def block_size(self) -> int: ...
    @property
    def name(self) -> str: ...
    @property
    def seed(self) -> int: ...

@final
class xxh32(_Hasher): ...

@final
class xxh3_64(_Hasher): ...

@final
class xxh3_128(_Hasher): ...

xxh64 = xxh3_64
xxh128 = xxh3_128

def xxh32_digest(args: _InputType, seed: int = ...) -> bytes: ...
def xxh32_hexdigest(args: _InputType, seed: int = ...) -> str: ...
def xxh32_intdigest(args: _InputType, seed: int = ...) -> int: ...

def xxh3_64_digest(args: _InputType, seed: int = ...) -> bytes: ...
def xxh3_64_hexdigest(args: _InputType, seed: int = ...) -> str: ...
def xxh3_64_intdigest(args: _InputType, seed: int = ...) -> int: ...

def xxh3_128_digest(args: _InputType, seed: int = ...) -> bytes: ...
def xxh3_128_hexdigest(args: _InputType, seed: int = ...) -> str: ...
def xxh3_128_intdigest(args: _InputType, seed: int = ...) -> int: ...

xxh64_digest = xxh3_64_digest
xxh64_hexdigest = xxh3_64_hexdigest
xxh64_intdigest = xxh3_64_intdigest

xxh128_digest = xxh3_128_digest
xxh128_hexdigest = xxh3_128_hexdigest
xxh128_intdigest = xxh3_128_intdigest
